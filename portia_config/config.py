from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager

_WEBDRIVER_OPTIONS: Options = Options()
_WEBDRIVER_OPTIONS.add_argument('--headless')
_WEBDRIVER: WebDriver = webdriver.Chrome(
    ChromeDriverManager(
        cache_valid_range=1,
        log_level=0,
        print_first_line=False
    ).install(),
    options=_WEBDRIVER_OPTIONS
)


def get_chrome_driver() -> WebDriver:
    global _WEBDRIVER
    return _WEBDRIVER


def set_chrome_driver(
        cache_valid_range: int,
        options: Options,
        log_level: int,
        print_first_line: bool
):

    global _WEBDRIVER

    _WEBDRIVER = webdriver.Chrome(
        ChromeDriverManager(
            cache_valid_range=cache_valid_range,
            log_level=log_level,
            print_first_line=print_first_line
        ).install(),
        options=options
    )
