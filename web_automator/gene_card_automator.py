from portia_config import config
from web_scrapper import scrapper as sc
from selenium import webdriver as wd
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from bs4 import Tag
from bs4 import ResultSet


def _drive(url: str) -> WebDriver:

    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver: WebDriver = wd.Chrome(
        chrome_options=chrome_options, executable_path=config.get_chrome_drive_destination())
    driver.get(url)
    driver_content: WebDriver = driver.page_source
    driver.close()

    return driver_content


def get_entrez_id(url: str) -> str:

    web_driver: WebDriver = _drive(url)
    dom: BeautifulSoup = BeautifulSoup(web_driver, "lxml")
    div_content: Tag = sc.get_div_content(
        dom, attrs={"class": "gc-subsection-inner-wrap"})
    links: ResultSet = div_content.find_all("a")

    return links[1].text
