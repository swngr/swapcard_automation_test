import time

from selenium.webdriver.common.by import By
from pages.base_page import Basepage
from utils.helpers import extract_rating_from_aria_label

class ShoppingPage(Basepage):

    button_refine_results = (By.XPATH, "//span[contains(@class, 'FzQmNc')]")
    link_price_high_to_low = By.XPATH, "//div[contains(@title,'high to low')]"
    textbox_max_price = By.XPATH, "//input[contains(@title,'Max')]"
    button_apply = (By.XPATH, "//button[contains(text(),'Apply') or contains(text(),'Go')]")
    product_cards = By.XPATH, "//div[@class='UC8ZCe QS8Cxb']"
    product_with_rating = By.XPATH, "//div[contains(@class,'UC8ZCe QS8Cxb')]//span[contains(@aria-label, 'Rated')]"

    def sort_high_to_low(self):
        time.sleep(0.3)
        self.click(*self.button_refine_results)
        self.click(*self.link_price_high_to_low)

    def set_price_filter(self, max_price):
        self.scroll_to_locator(*self.textbox_max_price)
        price_input = self.find(*self.textbox_max_price)
        price_input.clear()
        price_input.send_keys(str(max_price))
        self.click(*self.button_apply)

    def get_second_product_rating(self, min_rating):
        # Locate all elements with rating text (e.g., "Rated 4.6 out of 5")
        rating_elements = self.find_all(*self.product_with_rating)
        product_cards = self.find_all(*self.product_cards)
        print(f"[DEBUG] Found {len(rating_elements)} elements with rating")
        rating_elements_length = len(rating_elements)
        product_cards_length = len(product_cards)

        # Extract all rating values
        rating_values = []
        for idx, el in enumerate(rating_elements):
            try:
                rating_text = el.get_attribute("aria-label")  # e.g. "Rated 4.6 out of 5"
                rating_value = extract_rating_from_aria_label(rating_text)

                if idx % 2 == 0:  # Only even indexes to avoid duplicates
                    print(f"[DEBUG] EVEN Index {idx}: Rating = {rating_value}")
                    self.driver.execute_script("arguments[0].style.border='2px solid green'", el) # Highlight all found products in Green 🟩
                    rating_values.append(rating_value)
                else:
                    print(f"[DEBUG] ODD Index {idx}: Skipping")

            except Exception as e:
                print(f"[DEBUG] Failed to extract rating from element #{idx + 1}: {e}")
                continue

        rating_values

        if len(rating_values) < 2:
            raise Exception("Less than 2 rated products found.")

        # ✅ Check all ratings from the second onward
        bigger_equals_ratings = [
            {"index": i + 2, "rating": r}
            for i, r in enumerate(rating_values[2:])  # skip first two indexes due to duplication
            if r >= min_rating
        ]

        # Log ratings above min_rating
        if bigger_equals_ratings:
            print(f"[INFO] Products with rating bigger or equals to {min_rating}: {bigger_equals_ratings}")

        return {
            "from_second_rating_onwards": rating_values[2],
            "passed_ratings": bigger_equals_ratings
        }


        # Checking what ratings are below the threshold
        # ✅ Check all ratings from the second onward
        # failing_ratings = [
        #     {"index": i + 2, "rating": r}
        #     for i, r in enumerate(rating_values[1:])  # skip first
        #     if r < min_rating
        # ]
        #
        # # Log failing ratings, but don’t raise
        # if failing_ratings:
        #     print(f"[INFO] Products with rating below {min_rating}: {failing_ratings}")
        #
        # return {
        #     "second_rating": rating_values[1],
        #     "failing_ratings": failing_ratings
        # }