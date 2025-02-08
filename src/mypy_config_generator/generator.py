import re

import bs4

from .configuration import (
    ADJUSTED_CONFIGURATION_FILE,
    CONFIGURATION_FILE,
    OVERRIDE_DEFAULT_VALUES,
    SETTINGS_HTML_FILE,
    STRICT_STRING,
)


class Setting:
    """
    Single mypy setting.
    """

    def __init__(self) -> None:
        self.name: str | None = None
        self.default_value: str | None = None
        self.comments: list[str] = []

    def __str__(self) -> str:
        lines: list[str] = []
        lines.extend(self.get_comment_lines())
        if self.default_value in {'None', 'null', None}:
            lines.append(f'#{self.name} =')
        else:
            lines.append(f'{self.name} = {self.default_value}')
        lines.append('')
        return '\n'.join(lines)

    def get_comment_lines(self) -> list[str]:
        """
        Generate a list of comment lines.

        :return: list of comment lines
        """
        return [f'# {line}'.strip() for comment in self.comments for line in comment.splitlines()]


class Section:
    """
    Single mypy configuration section.
    """

    def __init__(self, name: str) -> None:
        self.name = name
        self.settings: list[Setting] = []

    def __str__(self) -> str:
        lines: list[str] = []
        lines.append(f'### {self.name}')
        lines.extend(str(setting) for setting in self.settings)
        lines.append('')
        return '\n'.join(lines)


class MypyConfiguration:
    """
    Whole Mypy configuration.
    """

    def __init__(self, version: str) -> None:
        self.version = version
        self.sections: list[Section] = []

    def new_section(self, name: str) -> None:
        """
        Start new section.

        :param name: section name
        """
        self.sections.append(Section(name))

    def new_setting(self, name: str, default_value: str | None, comments: list[str]) -> None:
        """
        Add new setting to latest section.

        :param name: setting's name
        :param default_value: setting's default value
        :param comments: setting's comment
        """
        setting = Setting()
        setting.name = name
        setting.default_value = default_value
        setting.comments = comments
        self.sections[-1].settings.append(setting)

    def update_default_values(self, update: dict[str, str]) -> None:
        """
        Update default values in settings according to provided dict.

        :param update: new default values for settings
        """
        update = update.copy()
        for section in self.sections:
            for setting in section.settings:
                if setting.name in update:
                    setting.default_value = update.pop(setting.name)
        if update:
            print(f'Not found overrides: {update}')  # noqa: T201

    def __str__(self) -> str:
        lines: list[str] = []
        lines.append(f'### Configuration created for mypy=={self.version}')
        lines.append('')
        lines.append('[mypy]')
        lines.append('')
        for section in self.sections:
            if not section.settings:
                continue
            lines.append(str(section))
        lines.append("""\
# This section should only define values that are different than in global section
[mypy-tests.*]
disallow_untyped_defs = False
disallow_incomplete_defs = False


# Conftests should be checked in the same manner as production code, so they revert `tests.*` overwrites
[mypy-tests.*.conftest]
disallow_untyped_defs = True
disallow_incomplete_defs = True
""")
        return '\n'.join(lines)


def generate_configuration() -> None:
    """
    Generate configuration file.
    """
    e_page = bs4.BeautifulSoup(SETTINGS_HTML_FILE.read_text(encoding='utf-8'), 'html.parser')
    (e_article,) = list(e_page.find_all('article'))
    assert isinstance(e_article, bs4.Tag)
    e_main_section = e_article.findChild('section')
    assert isinstance(e_main_section, bs4.Tag)
    version = re.search(r'mypy (\d+\.\d+.\d+) documentation', e_page.find('title').text).groups()[0]  # type: ignore [union-attr]
    config = MypyConfiguration(version)
    for e_section in e_main_section.findChildren('section'):
        section_name = e_section.findChild('h2').contents[0]
        config.new_section(section_name)
        for e_setting in e_section.find_all('dl', class_='confval'):
            setting_name = e_setting.find('span', class_='sig-name').text
            default_value = None
            e_setting_description = e_setting.findChild('dd')
            assert isinstance(e_setting_description, bs4.Tag)
            for e_title in e_setting_description.findChildren('dt'):
                assert isinstance(e_title, bs4.Tag)
                if e_title.text != 'Default:':
                    continue
                e_content = e_title.find_next_sibling()
                assert isinstance(e_content, bs4.Tag)
                default_value = e_content.text.strip()
            comments = [
                e_paragraph.text for e_paragraph in e_setting_description.findChildren('p', recursive=False)
            ]
            config.new_setting(setting_name, default_value, comments)
    CONFIGURATION_FILE.write_text(str(config))

    def _parse_flag(flag: str) -> tuple[str, str]:
        if flag.startswith('no_'):
            return flag[3:], 'False'
        return flag, 'True'

    overrides = OVERRIDE_DEFAULT_VALUES | dict(
        _parse_flag(flag.strip('-').replace('-', '_'))
        for flag in ''.join(line.strip() for line in STRICT_STRING.splitlines()).split(', ')
    )
    config.update_default_values(overrides)
    ADJUSTED_CONFIGURATION_FILE.write_text(str(config))
