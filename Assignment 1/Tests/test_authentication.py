from time import sleep

import pytest
from selenium.webdriver import Keys
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures("setup")
class TestLogin:
    driver: WebDriver

    def test_login(self):
        try:
            sleep(5)
            assert "Boards" in self.driver.title
        except Exception:
            assert False, "Login Not Successful"