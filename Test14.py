import allure
from selenium.webdriver.common.by import By

from base import *

#Url
driver.get('http://uitestingplayground.com/SampleApp')

# Elements
user_name_txt = driver.find_element(By.NAME, "UserName")
password_txt = driver.find_element(By.NAME, "Password")
login_btn = driver.find_element(By.CSS_SELECTOR, ".btn.btn-primary")
login_status = driver.find_element(By.ID, "loginstatus")

# Login Action
def login_action(user_name, password):
    user_name_txt.send_keys(user_name)
    password_txt.send_keys(password)
    login_btn.click()


class Test14_SimpalApp:
    def test_login(self):
        user_name = "Almog81"
        expected = "Welcome, " + user_name + "!"
        login_action(user_name, "pwd")
        result = login_status.text
        verifai_txt(expected, result)

    def test_logout(self):
        expected = "User logged out."
        if login_btn.text == "Log In":
            login_action("Almog81", "pwd")
        login_btn.click()
        result = login_status.text
        verifai_txt(expected, result)

    def test_login_failure(self):
        expected = "Invalid username/password"
        if login_btn.text == "Log Out":
            login_btn.click()
        login_action("Almog81", "KUKU")
        result = login_status.text
        verifai_txt(expected, result)
