from time import sleep
from typing import List
from selenium.webdriver.chrome.webdriver import WebDriver
from portia_config.config import PortiaConfig


config = PortiaConfig()


def get_article_citation(tag_list):

    driver: WebDriver = config.get_headed_chrome_driver()
    citation: List[str] = []

    for tag in tag_list:
        article_link = "https://pubmed.ncbi.nlm.nih.gov" + tag
        driver.get(article_link)
        driver.find_element_by_css_selector('.citation-button').click()
        sleep(5)

        try:
            citation.append(str(driver.find_element_by_css_selector('.citation-text').text).strip())
        # TODO: fix this
        except Exception:
            print(Exception)
            citation.append(' ')

    driver.close()

    return citation
