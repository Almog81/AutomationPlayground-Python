from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from base import *


def test01_dynamic_id():
    driver.get('http://uitestingplayground.com/dynamicid')
    btn = driver.find_element(By.XPATH, "//div[@class='container']/Button")
    verifai_txt("Button with Dynamic ID", btn.text)


def test02_class_attr():
    driver.get('http://uitestingplayground.com/classattr')
    expected = "Primary button pressed"
    driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()
    alr = driver.switch_to.alert
    result = alr.text
    alr.accept()
    verifai_txt(expected, result)


def test03_hidden_layers():
    driver.get('http://uitestingplayground.com/hiddenlayers')
    driver.find_element(By.CSS_SELECTOR, ".btn-success").click()
    driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()

    try:
        driver.find_element(By.CSS_SELECTOR, ".btn-success").click()
        pytest.fail("Green Button not supposed to Be Hit Twice!")
        screenshot("Green Button not supposed to Be Hit Twice!")
    except Exception:
        print("Green Button Can not Be Hit Twice!")
        pass


def test04_load_delay():
    driver.get('http://uitestingplayground.com/')
    expected = "http://uitestingplayground.com/loaddelay"
    driver.find_element(By.LINK_TEXT, "Load Delay").click()
    wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, '.btn-primary')))
    result = driver.current_url
    verifai_txt(expected, result)


def test05_AJAX_Data():
    driver.get('http://uitestingplayground.com/ajax')
    expected = "Data loaded with AJAX get request."
    driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()
    wait.until(ec.visibility_of_element_located((By.CLASS_NAME, 'bg-success')))
    result = driver.find_element(By.CLASS_NAME, 'bg-success').text
    verifai_txt(expected, result)


def test06_client_side_delay():
    driver.get('http://uitestingplayground.com/clientdelay')
    expected = "Data calculated on the client side."
    driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()
    result = driver.find_element(By.CLASS_NAME, 'bg-success').text
    verifai_txt(expected, result)


def test07_click():
    driver.get('http://uitestingplayground.com/click')
    expected = "btn btn-success"
    button = driver.find_element(By.ID, "badButton")
    action.move_to_element(button).click().perform()
    result = button.get_attribute("class")
    verifai_txt(expected, result)


def test08_text_input():
    driver.get('http://uitestingplayground.com/textinput')
    expected = "Almog Noach"
    driver.find_element(By.ID, "newButtonName").send_keys(expected)
    button = driver.find_element(By.ID, "updatingButton")
    button.click()
    result = button.text
    verifai_txt(expected, result)


def test09_scrollbars():
    driver.get('http://uitestingplayground.com/scrollbars')
    expected = "Hiding Button"
    hiding_btn = driver.find_element(By.CSS_SELECTOR, ".btn.btn-primary")
    driver.execute_script("arguments[0].scrollIntoView(true);", hiding_btn)
    result = hiding_btn.text
    verifai_txt(expected, result)


def test10_dynamic_table():
    driver.get('http://uitestingplayground.com/DynamicTable')
    expected = driver.find_element(By.CLASS_NAME, "bg-warning").text.split(": ")[1]
    columns = driver.find_elements(By.XPATH, "//span[@role='columnheader']")
    cells = driver.find_elements(By.XPATH, "//span[@role='cell']")
    result, x, y = "0", 0, 0
    for colum in columns:
        if colum.text == "CPU":
            break
        else:
            x = x + 1
    for cell in cells:
        if cell.text == "Chrome":
            y = y + x
            break
        else:
            y = y + 1
    result = cells[y].text
    verifai_txt(expected, result)


def test11_verify_text():
    driver.get('http://uitestingplayground.com/verifytext')
    expected = "Welcome UserName!"
    result = driver.find_element(By.XPATH, "//span[normalize-space(.)='Welcome UserName!']").text
    verifai_txt(expected, result)


def test12_progressbar():
    driver.get('http://uitestingplayground.com/progressbar')
    expected = "75%"
    start_btn = driver.find_element(By.ID, "startButton")
    stop_btn = driver.find_element(By.ID, "stopButton")
    progress_bar = driver.find_element(By.ID, "progressBar")
    start_btn.click()
    now = progress_bar.text
    while now != "75%":
        now = progress_bar.text
    stop_btn.click()
    result = progress_bar.text
    verifai_txt(expected, result)


def test13_visibility():
    driver.get('http://uitestingplayground.com/visibility')
    hide_btn = driver.find_element(By.ID, "hideButton")
    buttons = driver.find_elements(By.XPATH, "//button[@type=\"button\"]")

    # Create a list of buttons id names
    visible_btn_id = []
    for btn in buttons:
        visible_btn_id.append(btn.get_attribute("id"))

    # Click on Hide Button
    hide_btn.click()
    buttons = driver.find_elements(By.XPATH, "//button[@type=\"button\"]")

    # Create a new list of buttons id names after hide_btn click
    new_btn_id = []
    for btn in buttons:
        new_btn_id.append(btn.get_attribute("id"))
    hide_btn.click()

    # Checking if The Button Exist
    for btn in visible_btn_id:
        try:
            x = new_btn_id.index(btn)
            print(str(x) + ". " + btn + " fond but not visible")
        except ValueError:
            print(str(x) + ". " + btn + "  not fond")

    expected = 8
    result = len(buttons)
    verifai_txt(expected, result)
