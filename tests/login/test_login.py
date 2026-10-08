import pytest
from playwright.sync_api import Page, expect



@pytest.mark.smoke
def test_login_valid_credentials(page: Page):
    """TC-LOGIN-001 | SC-LOGIN-001 | REQ-LOGIN-01"""
    page.goto("https://www.saucedemo.com/")
    expect(page).to_have_title("Swag Labs")
    page.locator("#user-name").fill("standard_user")
    page.locator("#password").fill("secret_sauce")
    page.locator("#login-button").click()


    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
    expect(page.locator('[data-test="inventory-container"]')).to_be_visible()


