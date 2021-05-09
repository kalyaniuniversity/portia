import atexit
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager


class PortiaConfig:

    def __init__(self):
        self._options = Options()
        self._options.add_argument('--headless')
        self._web_driver: WebDriver or None = None
        self._headed_web_driver: WebDriver or None = None
        atexit.register(self.cleanup)

    def get_chrome_driver(self) -> WebDriver:
        if self._web_driver is None:
            self._web_driver = webdriver.Chrome(
                ChromeDriverManager(
                    cache_valid_range=1,
                    log_level=0,
                    print_first_line=False
                ).install(),
                options=self._options
            )
        return self._web_driver

    def set_chrome_driver(
            self,
            cache_valid_range: int,
            options: Options,
            log_level: int,
            print_first_line: bool
    ):
        self._web_driver = webdriver.Chrome(
            ChromeDriverManager(
                cache_valid_range=cache_valid_range,
                log_level=log_level,
                print_first_line=print_first_line
            ).install(),
            options=options
        )

    def close_driver(self):
        if self._web_driver is not None:
            self._web_driver.close()

    def get_headed_chrome_driver(self) -> WebDriver:
        if self._headed_web_driver is None:
            self._headed_web_driver = webdriver.Chrome(
                ChromeDriverManager(
                    cache_valid_range=1,
                    log_level=0,
                    print_first_line=False
                ).install()
            )
        return self._headed_web_driver

    def set_headed_chrome_driver(
            self,
            cache_valid_range: int,
            options: Options,
            log_level: int,
            print_first_line: bool
    ):
        self._headed_web_driver = webdriver.Chrome(
            ChromeDriverManager(
                cache_valid_range=cache_valid_range,
                log_level=log_level,
                print_first_line=print_first_line
            ).install(),
            options=options
        )

    def close_headed_driver(self):
        if self._headed_web_driver is not None:
            self._headed_web_driver.close()

    def cleanup(self):
        self.close_driver()
        self.close_headed_driver()
