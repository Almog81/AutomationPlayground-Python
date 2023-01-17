from base import *


class Test14_SimpalApp:

    def test_login(self):
        driver.get('http://uitestingplayground.com/SampleApp')
        # Elements
        user_name_txt = driver.find_element(By.NAME, "UserName")
        password_txt = driver.find_element(By.NAME, "Password")
        login_btn = driver.find_element(By.CSS_SELECTOR, ".btn.btn-primary")
        login_status = driver.find_element(By.ID, "loginstatus")

        # User Info
        user_name = "Almog81"
        password = "pwd"

        # Login Test
        expected = "Welcome, " + user_name + "!"
        user_name_txt.send_keys(user_name)
        password_txt.send_keys(password)
        login_btn.click()
        result = login_status.text
        verifai_txt(expected, result)