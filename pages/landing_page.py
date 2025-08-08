from selenium.webdriver.common.by import By
from pages.base_page import Basepage
import time

class LandingPage(Basepage):
    URL = "https://www.google.com"

    textbox_search = (By.NAME, "q")
    link_shopping = (By.XPATH, "//Span[normalize-space()='Shopping']")

    def go_to_url(self):
        self.driver.get(self.URL)

    def search_for_book(self, book_name):
        self.go_to_url()
        self.type_slowly(*self.textbox_search, f"book {book_name}")
        self.find(*self.textbox_search).submit()

    def click_on_shopping_link(self):
        self.click(*self.link_shopping)

    def type_slowly(self, by, value, text):
        el = self.find(by, value)
        el.clear()
        for char in text:
            el.send_keys(char)
            time.sleep(0.5)  # delay between keystrokes to simulate real interaction