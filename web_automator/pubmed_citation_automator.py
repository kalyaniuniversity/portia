import requests
from bs4 import BeautifulSoup
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from portia_config import config_for_pubmed as config


def get_article_citation(tag_list):

    driver: WebDriver = config.get_chrome_driver()
    citation: List[str] = []

    for tag in tag_list:
        article_link = "https://pubmed.ncbi.nlm.nih.gov" + tag
        driver.get(article_link)
        driver.find_element_by_css_selector('.citation-button').click()
        sleep(5)

        try:
            citation.append(str(driver.find_element_by_css_selector(
                '.citation-text').text).strip())
        except Exception:
            print(Exception)
            citation.append(' ')

    driver.close()
    return citation
