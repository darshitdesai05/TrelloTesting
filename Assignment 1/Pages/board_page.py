from time import sleep

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

from Tests.credentials import boards_url


def is_board_page_displayed(driver: WebDriver) -> bool:
    return "Boards" in driver.title


def is_selected_board_displayed(driver: WebDriver, boardname: str) -> bool:
    sleep(5)
    return boardname in driver.title


def select_board(driver: WebDriver, boardname: str) -> bool:
    navigate_to_boards_page(driver)
    boards = driver.find_elements(By.CLASS_NAME, "board-tile-details-name")
    for board in boards:
        if board.text == boardname:
            board.click()
            return True
    return False


def navigate_to_boards_page(driver: WebDriver):
    driver.get(boards_url)
    sleep(3)

# //*[@id="board"]/li[2]/div/div[1]/div[1]/h2
# //*[@id="board"]/li[1]/div/div[1]/div[1]/h2
