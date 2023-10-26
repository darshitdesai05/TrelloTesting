from time import sleep

import pytest
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

from Tests.credentials import email, password


def logout(driver: WebDriver):
    pass


@pytest.fixture(scope="class")
def setup(request):
    driver: WebDriver = webdriver.Chrome()
    driver.get("http://trello.com")
    driver.implicitly_wait(10)
    driver.maximize_window()
    login(driver)
    request.cls.driver = driver
    yield
    logout(driver)
    request.cls.driver.close()


def login(driver: WebDriver):
    driver.find_element(By.XPATH,
                        "//div[@data-active='false']//div//div//a[contains(text(),'Log in')]").click()
    sleep(2)
    email_element = driver.find_element(By.NAME, "username")
    email_element.send_keys(email)
    email_element.send_keys(Keys.ENTER)
    password_element = driver.find_element(By.NAME, "password")
    password_element.send_keys(password)
    password_element.send_keys(Keys.ENTER)
    sleep(15)
