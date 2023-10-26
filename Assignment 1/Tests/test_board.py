from time import sleep

import pytest
from selenium.common import NoSuchElementException
from selenium.webdriver import Keys
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait

from Pages.board_page import is_selected_board_displayed, select_board, navigate_to_boards_page


@pytest.mark.usefixtures("setup")
class TestBoard:
    boardname = "test"
    listname = "testList1"
    cardName = "card1"
    driver: WebDriver

    def test_create_board(self):

        navigate_to_boards_page(self.driver)

        self.driver.find_element(By.XPATH, "//div[@class='board-tile mod-add']").click()
        board_title = self.driver.find_element(By.XPATH, "//input[@type='text']")
        board_title.send_keys(self.boardname)
        sleep(2)
        board_title.send_keys(Keys.ENTER)
        # buttons = self.driver.find_elements(By.TAG_NAME, "button")
        #
        # for button in buttons:
        #     if button.text == "Create":
        #         button.click()
        #         break
        sleep(5)

        assert self.boardname in self.driver.title

    def test_add_list(self):
        navigate_to_boards_page(self.driver)
        if not is_selected_board_displayed(self.driver, self.boardname):
            if not select_board(self.driver, self.boardname):
                assert False, "Board does not exist"
        try:
            add_list_button: WebElement = WebDriverWait(self.driver, 13).until(
                lambda x: x.find_element(By.XPATH, '//*[@id="board"]/div/button')
            )
            add_list_button.click()
            list_title = self.driver.find_element(
                By.XPATH,
                '//*[@id="board"]/div[1]/form/textarea')
            list_title.send_keys(self.listname)
            list_title.send_keys(Keys.ENTER)
            list_elements = self.driver.find_elements(By.TAG_NAME, "h2")
            added = False
            for list_element in list_elements:
                if list_element.text == self.listname:
                    added = True
            assert added, "Failed to add a list"
        except NoSuchElementException:
            assert False, "Find the list element."

    def test_add_card_to_list(self):
        # //*[@id="board"]/li[2]/div/div[2]/button[1]
        # //*[@id="board"]/li[1]/div/div[2]/button[1]
        # //*[@id="board"]

        if not select_board(self.driver, self.boardname):
            assert False, "Board Not Found"

        try:
            try:
                first_list = self.driver.find_element(By.XPATH, '//*[@id="board"]/li[1]/div/div[1]/div[1]/h2')
                add_card_btn = self.driver.find_element(By.XPATH, '//*[@id="board"]/li[1]/div/div[2]/button[1]')
            except NoSuchElementException:
                add_card_btn = self.driver.find_element(By.XPATH, '//*[@id="board"]/div/button')

            add_card_btn.click()

            enter_card_name = self.driver.find_element(By.XPATH, '//*[@id="board"]/li[1]/div/ol/form/textarea')
            enter_card_name.send_keys(self.cardName)
            enter_card_name.send_keys(Keys.ENTER)

            card_list = self.driver.find_elements(By.XPATH, '//*[@id="board"]/li[1]/div/ol/li/div/div/a')
            card_texts = [card.text for card in card_list]
            assert any(card_text == self.cardName for card_text in card_texts), "Card not added"

            # //*[@id="board"]/li[1]/div/ol/li[1]/div/div/a
            # //*[@id="board"]/li[1]/div/ol/li[2]/div/div/a
        except NoSuchElementException:
            assert False, "List Not Found to Add Card"