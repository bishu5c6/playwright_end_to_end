# we are going to work by using built in locators.

from playwright.sync_api import Page, expect
import time

def test_built_in_locators(page:Page):
    # page.getByAltText()
    page.goto("https://www.nopcommerce.com/en/demo?srsltid=AfmBOoojDavOkz8JeO3KjMW99_2Vh-CYvVCGATa9Bv1iTn98FiRekcl7")
    logo=page.get_by_alt_text("nopCommerce")
    expect(logo).to_be_visible()
    time.sleep(4)
    page.wait_for_timeout(5000)
    # pytest -v -s test_playwright_built_in_locators.py --headed
