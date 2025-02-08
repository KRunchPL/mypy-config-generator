import requests

from .configuration import SETTINGS_HTML_FILE


_SETTINGS_HTML_URL = 'https://mypy.readthedocs.io/en/stable/config_file.html'
_REQUEST_TIMEOUT = 10  # in seconds


def download_settings_page() -> None:
    """
    Download mypy's settings page as HTML.
    """
    response = requests.get(_SETTINGS_HTML_URL, timeout=_REQUEST_TIMEOUT)
    SETTINGS_HTML_FILE.write_text(response.text, encoding='utf-8')
