# ruff: noqa: E501
from pathlib import Path


WORKDIR = Path('workdir')
SETTINGS_HTML_FILE = WORKDIR / 'settings.html'
VERSION_FILE = WORKDIR / 'version.txt'
CONFIGURATION_FILE = WORKDIR / 'mypy.ini'
ADJUSTED_CONFIGURATION_FILE = WORKDIR / 'mypy_adjusted.ini'
STRICT_STRING = """\
--warn-unused-configs, --disallow-any-generics, --disallow-subclassing-any, --disallow-untyped-calls, --disallow-
                            untyped-defs, --disallow-incomplete-defs, --check-untyped-defs, --disallow-untyped-decorators, --warn-redundant-casts, --warn-unused-ignores, --warn-return-
                            any, --no-implicit-reexport, --strict-equality, --extra-checks
"""
OVERRIDE_DEFAULT_VALUES = {
    'files': '.',
    'strict': 'True',
    'warn_unreachable': 'True',
    'strict_concatenate': 'True',
    'warn_incomplete_stub': 'True',
}
