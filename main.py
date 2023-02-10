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
        time.sleep(1)
        self.weight = self.driver.find_element(By.ID, "weight")
        self.height = self.driver.find_element(By.ID, "height")
        self.calculate_btn = self.driver.find_element(
            By.CLASS_NAME, "calculate-btn")

    def test_bmi_nan(self):
        """Test an invalid BMI result that should result in NaN and should not be accepted."""
        self.weight.send_keys('0')
        self.height.send_keys('0')
        time.sleep(1)
        self.calculate_btn.click()
        time.sleep(1)
        container_items = self.driver.find_elements(
            By.CSS_SELECTOR, "..data-container col")
        self.assertEqual(len(container_items), 0)

    def test_bmi_inf(self):
        """Test an invalid BMI result that should result in Inf and should not be accepted."""
        self.weight.send_keys('10')
        self.height.send_keys('0')
        time.sleep(1)
        self.calculate_btn.click()
        time.sleep(1)
        container_items = self.driver.find_elements(
            By.CSS_SELECTOR, ".data-container col")
        self.assertEqual(len(container_items), 0)

    def test_bmi_zero(self):
        """Test an invalid BMI result that should result in 0 and should not be accepted."""
        self.weight.send_keys('0')
        self.height.send_keys('10')
        time.sleep(1)
        self.calculate_btn.click()
        time.sleep(1)
        container_items = self.driver.find_elements(
            By.CSS_SELECTOR, ".data-container col")
        self.assertEqual(len(container_items), 0)

    def test_bmi_normal(self):
        """Test a valid BMI score."""
        self.weight.send_keys('80')
        self.height.send_keys('185')
        time.sleep(1)
        self.calculate_btn.click()
        time.sleep(1)
        container_items = self.driver.find_elements(
            By.CSS_SELECTOR, ".data-container col")
        self.assertEqual(len(container_items), 1)

    def tearDown(self):
        self.driver.close()


class BMIStorage(unittest.TestCase):
    """A sample test class to test how the BMI results storage works"""

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
        # self.data_container = self.driver.find_element(By.CSS_SELECTOR, ".data-container col")

    def test_bmi_normal_add_remove(self):
        """Test whether the delete functionality works correctly"""
        self.weight.send_keys('80')
        self.height.send_keys('185')
        time.sleep(1)
        self.calculate_btn.click()
        time.sleep(1)
        del_btn = self.driver.find_element(By.CLASS_NAME, "delete-btn")
        del_btn.click()
        time.sleep(1)
        container_items = self.driver.find_elements(
            By.CSS_SELECTOR, ".data-container col")
        self.assertEqual(len(container_items), 0)

    def test_bmi_undo_hidden(self):
        """Test whether the undo button remains hidden until the right time."""
        self.weight.send_keys('80')
        self.height.send_keys('185')
        time.sleep(1)
        self.calculate_btn.click()
        time.sleep(1)
        container_items = self.driver.find_elements(
            By.CLASS_NAME, "calculate-btn")
        self.assertEqual(len(container_items), 1)

    def test_bmi_undo_visible(self):
        """Test whether the undo button is being shown in the right time."""
        self.weight.send_keys('80')
        self.height.send_keys('185')
        time.sleep(1)
        self.calculate_btn.click()
        time.sleep(1)
        del_btn = self.driver.find_element(By.CLASS_NAME, "delete-btn")
        del_btn.click()
        time.sleep(1)
        container_items = self.driver.find_elements(
            By.CLASS_NAME, "calculate-btn")
        self.assertEqual(len(container_items), 2)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
