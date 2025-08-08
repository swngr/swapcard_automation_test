import pytest
import allure
from pages.landing_page import LandingPage
from pages.shopping_page import ShoppingPage
from utils.config import DEFAULT_BOOKS

@allure.feature("Google Shopping Test")
@allure.story("Verify ratings from second product onward")
@pytest.mark.parametrize("book_name,max_price,min_rating", DEFAULT_BOOKS)
def test_google_shopping_book(browser, book_name, max_price, min_rating):
    search_page = LandingPage(browser)
    shopping_page = ShoppingPage(browser)

    with allure.step("Navigate to Google, type the book's name and search for the book"):
        search_page.search_for_book(book_name="harry potter")

    with allure.step("Click on shopping, sort results from high to low and apply price filter"):
        search_page.click_on_shopping_link()
        shopping_page.sort_high_to_low()
        shopping_page.set_price_filter(max_price)

    with allure.step("Verify rated products from 2nd onward"):
        result = shopping_page.get_second_product_rating(min_rating=4.6)
        if result:
            allure.attach(
                str(result["from_second_rating_onwards"]),
                name="Ratings From Second Product Onwards",
                attachment_type=allure.attachment_type.TEXT
            )
            if result["passed_ratings"]:
                allure.attach(
                    str(result["passed_ratings"]),
                    name="Ratings Above Threshold",
                    attachment_type=allure.attachment_type.TEXT
                )
        else:
            allure.attach("No second rated product found", name="Warning", attachment_type=allure.attachment_type.TEXT)
