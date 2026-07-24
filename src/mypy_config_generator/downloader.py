import requests

from .app_config import AppConfiguration


_SETTINGS_HTML_URL = 'https://mypy.readthedocs.io/en/stable/config_file.html'
_REQUEST_TIMEOUT = 10  # in seconds


def download_settings_page(app_config: AppConfiguration) -> None:
    """
    Download mypy's settings page as HTML.

    :param app_config: application configuration
    """
    response = requests.get(_SETTINGS_HTML_URL, timeout=_REQUEST_TIMEOUT)
    app_config.settings_html_file.write_text(response.text, encoding='utf-8')
