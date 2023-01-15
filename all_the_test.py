import time

import pytest
from selenium import webdriver
from selenium.webdriver.common import alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains


driver = webdriver.Chrome()
wait = WebDriverWait(driver, 15)
action = ActionChains(driver)


@pytest.fixture(autouse=True, scope='session')
def init_test():
    driver.maximize_window()
    driver.implicitly_wait(20)
    yield
    # time.sleep(3)
    driver.quit()


def test01_dynamic_id():
    driver.get('http://uitestingplayground.com/dynamicid')
    btn = driver.find_element(By.XPATH, "//div[@class='container']/Button")
    assert btn.text == "Button with Dynamic ID"


def test02_class_attr():
    driver.get('http://uitestingplayground.com/classattr')
    ex_txt = "Primary button pressed"
    driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()
    alr = driver.switch_to.alert
    result_txt = alr.text
    alr.accept()
    assert ex_txt == result_txt


def test03_hidden_layers():
    driver.get('http://uitestingplayground.com/hiddenlayers')
    driver.find_element(By.CSS_SELECTOR, ".btn-success").click()
    driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()

    try:
        driver.find_element(By.CSS_SELECTOR, ".btn-success").click()
        pytest.fail("Green Button not supposed to Be Hit Twice!")
    except Exception as e:
        print("Green Button Can not Be Hit Twice!")
        pass


def test04_load_delay():
    driver.get('http://uitestingplayground.com/')
    url = "http://uitestingplayground.com/loaddelay"
    driver.find_element(By.LINK_TEXT, "Load Delay").click()
    wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, '.btn-primary')))
    result = driver.current_url
    assert url == result


def test05_AJAX_Data():
    driver.get('http://uitestingplayground.com/ajax')
    expected = "Data loaded with AJAX get request."
    driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()
    wait.until(ec.visibility_of_element_located((By.CLASS_NAME, 'bg-success')))
    result = driver.find_element(By.CLASS_NAME, 'bg-success').text
    assert expected == result


def test06_client_side_delay():
    driver.get('http://uitestingplayground.com/clientdelay')
    expected = "Data calculated on the client side."
    driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()
    result = driver.find_element(By.CLASS_NAME, 'bg-success').text
    assert expected == result


def test07_click():
    driver.get('http://uitestingplayground.com/click')
    expected = "btn btn-success"
    button = driver.find_element(By.ID, "badButton")
    action.move_to_element(button).click().perform()
    result = button.get_attribute("class")
    assert expected == result


def test08_text_input():
    driver.get('http://uitestingplayground.com/textinput')
    expected = "Almog Noach"
    driver.find_element(By.ID, "newButtonName").send_keys(expected)
    button = driver.find_element(By.ID, "updatingButton")
    button.click()
    result = button.text
    assert expected == result

