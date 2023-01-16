import time
import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains


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
