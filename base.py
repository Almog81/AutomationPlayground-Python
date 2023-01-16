import time
import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import allure
from allure_commons.types import AttachmentType

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 15)
action = ActionChains(driver)


@pytest.fixture(autouse=True, scope='session')
def init_test():
    driver.maximize_window()
    driver.implicitly_wait(20)
    yield
    time.sleep(3)
    driver.quit()


def verifai_txt(expected, result):
    try:
        assert expected == result
    except AssertionError:
        screenshot("Assert Error")
        assert False


def screenshot(name):
    allure.attach(driver.get_screenshot_as_png(), name=name, attachment_type=AttachmentType.PNG)
