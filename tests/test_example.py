import pytest
from playwright.sync_api import Page, expect
from pages.login_page import LoginPage
from tests.expected_texts import expected_texts

@pytest.mark.parametrize("lang,texts", list(expected_texts.items()))
def test_language_selector(page: Page, lang, texts):
    login_page = LoginPage(page)
    expect(login_page.language_div).to_be_visible()
    login_page.change_language(lang)
    expect(login_page.username_input).to_have_attribute("placeholder", texts['username'])
    expect(login_page.password_input).to_have_attribute("placeholder", texts['password'])
    expect(login_page.login_button).to_have_attribute("value", texts['login_button'])
    expect(login_page.login_forgot).to_have_text(texts['forgot_label'])
    checkbox_label = login_page.page.locator('label.checkbox:has(input#CheckBoxRemember)')
    expect(checkbox_label).to_contain_text(texts['remember_span'])

def test_refresh_page_language_selector(page: Page):
    login_page = LoginPage(page)
    expect(login_page.language_div).to_be_visible()

    lang_cookie = page.context.cookies()
    lang_value = None
    for cookie in lang_cookie:
        if cookie.get('name') == 'LANG':
            lang_value = cookie.get('value')
            break
    assert lang_value is not None, "LANG cookie not found!"

    page.reload()

    lang_cookie_after = page.context.cookies()
    lang_value_after = None
    for cookie in lang_cookie_after:
        if cookie.get('name') == 'LANG':
            lang_value_after = cookie.get('value')
            break
    assert lang_value_after is not None, "LANG cookie not found after refresh!"
    assert lang_value == lang_value_after, f"LANG cookie changed after refresh: {lang_value} -> {lang_value_after}"