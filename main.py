import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class BMICalculation(unittest.TestCase):
    """A sample test class to test how the BMI calculation works"""

    def setUp(self):
        self.driver = webdriver.Chrome(
            "C:\Program Files (x86)\chromedriver.exe")
        self.driver.maximize_window()
        self.driver.delete_all_cookies()
        self.driver.get("http://localhost:3000")
        time.sleep(3)
        self.weight = self.driver.find_element(By.ID, "weight")
        self.height = self.driver.find_element(By.ID, "height")
        self.calculate_btn = self.driver.find_element(
            By.CLASS_NAME, "calculate-btn")
        # self.data_container = self.driver.find_element(By.CLASS_NAME, "data-container")

    def test_bmi_nan(self):
        """."""
        self.weight.send_keys('0')
        self.height.send_keys('0')
        time.sleep(1)
        self.calculate_btn.click()
        time.sleep(1)
        container_items = self.driver.find_elements(
            By.CLASS_NAME, "data-container")
        self.assertEqual(len(container_items), 0)

    def test_bmi_inf(self):
        """."""
        self.weight.send_keys('10')
        self.height.send_keys('0')
        time.sleep(1)
        self.calculate_btn.click()
        time.sleep(1)
        container_items = self.driver.find_elements(
            By.CLASS_NAME, "data-container")
        self.assertEqual(len(container_items), 0)

    def test_bmi_zero(self):
        """."""
        self.weight.send_keys('0')
        self.height.send_keys('10')
        time.sleep(1)
        self.calculate_btn.click()
        time.sleep(1)
        container_items = self.driver.find_elements(
            By.CLASS_NAME, "data-container")
        self.assertEqual(len(container_items), 0)

    def test_bmi_normal(self):
        """."""
        self.weight.send_keys('80')
        self.height.send_keys('185')
        time.sleep(1)
        self.calculate_btn.click()
        time.sleep(1)
        container_items = self.driver.find_elements(
            By.CLASS_NAME, "data-container")
        print(len(container_items))
        self.assertEqual(len(container_items), 1)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
