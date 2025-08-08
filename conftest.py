import pytest
import os
import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # Execute all other hooks to obtain the report object
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        # Only take screenshots for tests that failed during the actual test run
        browser = item.funcargs.get("browser", None)
        if browser:
            screenshot_dir = "screenshots"
            os.makedirs(screenshot_dir, exist_ok=True)
            file_name = f"{item.name}.png"
            file_path = os.path.join(screenshot_dir, file_name)
            browser.save_screenshot(file_path)

            # Attach to Allure report if enabled
            if "allure" in item.config.pluginmanager.list_plugin_distinfo():
                allure.attach.file(file_path, name="screenshot", attachment_type=allure.attachment_type.PNG)

@pytest.fixture
def browser(request):
    headless = request.config.getoption("--headless")

    options = Options()
    if headless:
        options.add_argument("--headless=new")
        options.add_argument("--disable-gpu")
        options.add_argument("--window-size=1920,1080")

    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(5)
    yield driver
    driver.quit()

# Uncomment below and comment function above if You're Blocked by Google reCAPTCHA
# @pytest.fixture
# def browser():
#     options = Options()
#     options.debugger_address = "127.0.0.1:9222"  # Hook into existing Chrome
#     driver = webdriver.Chrome(options=options)
#     yield driver
#     driver.quit()

# Also useful if you want to support `--headless` from command line
def pytest_addoption(parser):
    parser.addoption("--headless", action="store_true", help="Run browser in headless mode")

