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



@pytest.mark.regression
def test_login_invalid_user_invalid_password(page: Page):
    """TC-LOGIN-002 | SC-LOGIN-002 | REQ-LOGIN-02"""
    page.goto("https://www.saucedemo.com/")
    expect(page).to_have_title("Swag Labs")
    page.locator("#user-name").fill("testing_saucedemo")
    page.locator("#password").fill("new_userTesting`")
    page.locator("#login-button").click()

    error = page.get_by_role("alert")
    expect(error).to_have_text('Epic sadface: Username and password do not match any user in this service')

    expect(page).to_have_url("https://www.saucedemo.com/")
    expect(page.locator('[data-test="inventory-container"]')).not_to_be_visible()


@pytest.mark.regression
def test_login_nonexistent_user_valid_password(page: Page):
    """TC-LOGIN-003 | SC-LOGIN-003 | REQ-LOGIN-02"""
    page.goto("https://www.saucedemo.com/")
    expect(page).to_have_title("Swag Labs")
    page.locator("#user-name").fill("testing_saucedemo")
    page.locator("#password").fill("secret_sauce")
    page.locator("#login-button").click()

    error = page.get_by_role("alert")
    expect(error).to_have_text('Epic sadface: Username and password do not match any user in this service')

    expect(page).to_have_url("https://www.saucedemo.com/")
    expect(page.locator('[data-test="inventory-container"]')).not_to_be_visible()




@pytest.mark.regression
def test_login_valid_user_invalid_password(page: Page):
    """TC-LOGIN-004 | SC-LOGIN-004 | REQ-LOGIN-02"""
    page.goto("https://www.saucedemo.com/")
    expect(page).to_have_title("Swag Labs")
    page.locator("#user-name").fill("standard_user")
    page.locator("#password").fill("secret_user_demo")
    page.locator("#login-button").click()

    error = page.get_by_role("alert")
    expect(error).to_have_text('Epic sadface: Username and password do not match any user in this service')

    expect(page).to_have_url("https://www.saucedemo.com/")
    expect(page.locator('[data-test="inventory-container"]')).not_to_be_visible()




@pytest.mark.regression
def test_login_empty_credentials(page: Page):
    """TC-LOGIN-005 | SC-LOGIN-005 | REQ-LOGIN-03"""
    page.goto("https://www.saucedemo.com/")
    expect(page).to_have_title("Swag Labs")
    page.locator("#user-name").fill("")
    page.locator("#password").fill("")
    page.locator("#login-button").click()

    error = page.get_by_role("alert")
    expect(error).to_have_text('Epic sadface: Username is required')

    expect(page).to_have_url("https://www.saucedemo.com/")
    expect(page.locator('[data-test="inventory-container"]')).not_to_be_visible()


@pytest.mark.regression
def test_login_valid_user_empty_password(page: Page):
    """TC-LOGIN-006 | SC-LOGIN-006 | REQ-LOGIN-03"""
    page.goto("https://www.saucedemo.com/")
    expect(page).to_have_title("Swag Labs")
    page.locator("#user-name").fill("standard_user")
    page.locator("#password").fill("")
    page.locator("#login-button").click()

    error = page.get_by_role("alert")
    expect(error).to_have_text('Epic sadface: Password is required')

    expect(page).to_have_url("https://www.saucedemo.com/")
    expect(page.locator('[data-test="inventory-container"]')).not_to_be_visible()


@pytest.mark.regression
def test_login_empty_user_valid_password(page: Page):
    """TC-LOGIN-007 | SC-LOGIN-007 | REQ-LOGIN-03"""
    page.goto("https://www.saucedemo.com/")
    expect(page).to_have_title("Swag Labs")
    page.locator("#user-name").fill("")
    page.locator("#password").fill("secret_sauce")
    page.locator("#login-button").click()

    error = page.get_by_role("alert")
    expect(error).to_have_text('Epic sadface: Username is required')

    expect(page).to_have_url("https://www.saucedemo.com/")
    expect(page.locator('[data-test="inventory-container"]')).not_to_be_visible()