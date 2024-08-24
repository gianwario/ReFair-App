from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class TestLoad:

    def test_load_tc_1(self, driver, load_tc_1_fixture):
        """
        Uploads an Excel file with an incorrect filename and verifies that an alert with the message 
        'The file name is not \"stories\"' is displayed.
        """
        expected_alert_message = "The file name is not \"stories\""

        driver.get("http://localhost:5173/")

        file_input = driver.find_element(By.CSS_SELECTOR, ".form-control")
        file_input.send_keys(load_tc_1_fixture)

        driver.find_element(By.CSS_SELECTOR, ".btn-info").click()

        try:
            alert = WebDriverWait(driver, 10).until(EC.alert_is_present())
            assert alert.text == expected_alert_message, f"Unexpected alert text: {alert.text}"
            alert.accept()
        except TimeoutException:
            assert False, "Alert with the message '" + \
                expected_alert_message + "' did not appear."


    def test_load_tc_2(self, driver, load_tc_2_fixture):
        """
        Uploads a .txt file and verifies that an alert with the message
        'This type of file is not supported. Upload an xlsx file.' is displayed.
        """
        expected_alert_message = "This type of file is not supported. Upload an xlsx file."

        driver.get("http://localhost:5173/")

        file_input = driver.find_element(By.CSS_SELECTOR, ".form-control")
        file_input.send_keys(load_tc_2_fixture)

        driver.find_element(By.CSS_SELECTOR, ".btn-info").click()

        try:
            alert = WebDriverWait(driver, 10).until(EC.alert_is_present())
            assert alert.text == expected_alert_message, f"Unexpected alert text: {alert.text}"
            alert.accept()
        except TimeoutException:
            assert False, "Alert with the message '" + \
                expected_alert_message + "' did not appear."


    def test_load_tc_3(self, driver, load_tc_3_fixture):
        """
        Uploads an Excel file with a single sheet and no columns, and verifies that an alert 
        with the message 'No column \"User Story\" found' is displayed.
        """
        expected_alert_message = "No column \"User Story\" found"

        driver.get("http://localhost:5173/")

        file_input = driver.find_element(By.CSS_SELECTOR, ".form-control")
        file_input.send_keys(load_tc_3_fixture)

        driver.find_element(By.CSS_SELECTOR, ".btn-info").click()

        try:
            alert = WebDriverWait(driver, 10).until(EC.alert_is_present())
            assert alert.text == expected_alert_message, f"Unexpected alert text: {alert.text}"
            alert.accept()
        except TimeoutException:
            assert False, "Alert with the message '" + \
                expected_alert_message + "' did not appear."


    def test_load_tc_4(self, driver, load_tc_4_fixture):
        """
        Uploads an Excel file with a single sheet and two columns (including "User Story"), 
        and verifies that an alert with the message 'The file must contain only a single column.'
        is displayed.
        """
        expected_alert_message = "The file must contain only a single column."

        driver.get("http://localhost:5173/")

        file_input = driver.find_element(By.CSS_SELECTOR, ".form-control")
        file_input.send_keys(load_tc_4_fixture)

        driver.find_element(By.CSS_SELECTOR, ".btn-info").click()

        try:
            alert = WebDriverWait(driver, 10).until(EC.alert_is_present())
            assert alert.text == expected_alert_message, f"Unexpected alert text: {alert.text}"
            alert.accept()
        except TimeoutException:
            assert False, "Alert with the message '" + \
                expected_alert_message + "' did not appear."
