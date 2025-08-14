import re
from playwright.sync_api import Page, expect
from pages.login_page import LoginPage

def test_language_selector(page: Page):
    login_page = LoginPage(page)
    page.goto("https://demo.biometric.sk/")
    # Example: login_page.login('user', 'pass')
    expect(page).to_have_title(re.compile("Prihlásenie do systému - Dochadzka.DEMO"))

def test_refresh_page_language_selector(page: Page):
    login_page = LoginPage(page)
    page.goto("https://demo.biometric.sk/")
    expect(page).to_have_title(re.compile("Prihlásenie do systému - Dochadzka.DEMO"))