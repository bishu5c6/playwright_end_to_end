# we are going to work by using built in locators.

from playwright.sync_api import Page, expect
import time
import re


# 1) page.get_by_alt_text()
# 2) page.get_by_text()
# 3) page.get_by_role()
# 4) page.get_by_label()
# 5) page.get_by_placeholder()
# 6) page.get_by_title()
# 7) page.get_by_test_id()

def test_built_in_locators(page:Page):
    #1) page.getByAltText()
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    logo=page.get_by_alt_text("company-branding")
    expect(logo).to_be_visible()


    #2) Page. get_by_ text
    expect(page.get_by_text("© 2005 - 2026 ")).to_be_visible()
    #you can use partial text and regular expression

    # 3) page.get_by_role()
    expect(page.get_by_role("heading", name="Login")).to_be_visible()

    #4) page.get_by_label
    page.get_by_label("Username").fill("admin", timeout=10000)
    page.get_by_label("Password").fill("admin123", timeout=10000)
    page.wait_for_timeout(5000)
    page.close()

   # pytest -v -s test_playwright_built_in_locators.py --headed