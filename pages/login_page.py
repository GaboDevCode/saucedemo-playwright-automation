from playwright.sync_api import Page


class LoginPage(Page):


    def __init__(self, page: Page):
        self.page = page
        self.username = page.locator("#user-name")
        self.password = page.locator("#password")
        self.login_button = page.locator("#login-button")
        self.error_message = page.get_by_role("alert")

    def navigate_to_login(self):
            self.page.goto("/")

    def login(self, username: str, password: str):
        self.username.fill(username)
        self.password.fill(password)
        self.login_button.click()

