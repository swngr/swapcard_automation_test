from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import os
import time

class Basepage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def find(self, by, value):
        return self.wait.until(EC.presence_of_element_located((by, value)))

    def find_all(self, by, value):
        return self.wait.until(EC.presence_of_all_elements_located((by, value)))

    def click(self, by, value):
        self.find(by, value).click()

    def type(self, by, value, text):
        el = self.find(by, value)
        el.clear()
        el.send_keys(text)

    def wait_for_visible(self, by, value):
        return self.wait.until(EC.visibility_of_element_located((by, value)))

    def take_screenshot(self, filename):
        timestamp = int(time.time())
        path = os.path.join("screenshots", f"{filename}_{timestamp}.png")
        self.driver.save_screenshot(path)
        return path

    def scroll_to_locator(self, by, value):
        element = self.driver.find_element(by, value)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
