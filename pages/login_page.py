from playwright.sync_api import Page

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.username_input = page.locator('input[id="TextBoxUsername"]')
        self.password_input = page.locator('input[id="TextBoxPassword"]')
        self.login_button = page.locator('input[id="Button1"]')
        self.language_div = page.locator('div[id="divJazykVlajky"]')
        self.login_forgot = page.locator('span[id="LabelForgetPassword"]')
        self.checkbox_remember = page.locator('checkbox[id="CheckBoxRemember"]')

    def change_language(self, language: str):
        items = self.language_div.locator('div.topbar-item a')
        count = items.count()
        for i in range(count):
            link = items.nth(i)
            img = link.locator('img')
            alt = img.get_attribute('alt')
            if alt and alt.lower() == language.lower():
                link.click()
                return
        raise ValueError(f"Language '{language}' not found in language_div.")
