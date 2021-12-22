import pytest
from selenium import webdriver
from helpers import CHROME_DRIVER_PATH


@pytest.fixture()
def chrome_browser():
    driver = webdriver.Chrome(CHROME_DRIVER_PATH)
    yield driver
    driver.close()