import pytest
from playwright.sync_api import Page, expect
from pages.login_page import LoginPage

@pytest.mark.smoke
def test_login_valid_credentials(page: Page):
    """TC-LOGIN-001 | SC-LOGIN-001 | REQ-LOGIN-01"""
    login_page = LoginPage(page)
    login_page.navigate_to_login()
    login_page.login("standard_user", "secret_sauce")

    expect(page).to_have_url("/inventory.html")
    expect(page.locator('[data-test="inventory-container"]')).to_be_visible()





INVALID_CREDENTIALS_ERROR = ("Epic sadface: Username and password do not match any user in this service")

@pytest.mark.regression
@pytest.mark.parametrize(
    "username, password",
    [
        pytest.param(
            "testing_saucedemo",
            "new_userTesting",
            id="TC-LOGIN-002-invalid_user_invalid_password",
        ),
        pytest.param(
            "testing_saucedemo",
            "new_userTesting",
            id="TC-LOGIN-003-nonexistent_user_valid_password",
        ),
        pytest.param(
            "testing_saucedemo",
            "new_userTesting",
             id="TC-LOGIN-004-valid_user_invalid_password",
        ),

    ]
    )


def test_login_invalid_credentials(page: Page, username: str, password: str):
    """SC-LOGIN-002/003/004 | REQ-LOGIN-02"""
    login_page = LoginPage(page)
    login_page.navigate_to_login()
    login_page.login(username, password)

    expect(login_page.error_message).to_have_text(INVALID_CREDENTIALS_ERROR)
    expect(page).to_have_url("/")
    expect(page.locator('[data-test="inventory-container"]')).not_to_be_visible()






@pytest.mark.regression
def test_login_empty_credentials(page: Page):
    """TC-LOGIN-005 | SC-LOGIN-005 | REQ-LOGIN-03"""
    login_page = LoginPage(page)
    login_page.navigate_to_login()
    login_page.login("", "")
    expect(login_page.error_message).to_have_text("Epic sadface: Username is required")
    expect(page).to_have_url("/")
    expect(page.locator('[data-test="inventory-container"]')).not_to_be_visible()


@pytest.mark.regression
def test_login_valid_user_empty_password(page: Page):
    """TC-LOGIN-006 | SC-LOGIN-006 | REQ-LOGIN-03"""
    login_page = LoginPage(page)
    login_page.navigate_to_login()
    login_page.login("standard_user", "")
    expect(login_page.error_message).to_have_text("Epic sadface: Password is required")
    expect(page).to_have_url("/")
    expect(page.locator('[data-test="inventory-container"]')).not_to_be_visible()





@pytest.mark.regression
def test_login_empty_user_valid_password(page: Page):
    """TC-LOGIN-007 | SC-LOGIN-007 | REQ-LOGIN-03"""
    login_page = LoginPage(page)
    login_page.navigate_to_login()
    login_page.login("", "secret_sauce")
    expect(login_page.error_message).to_have_text("Epic sadface: Username is required")
    expect(page).to_have_url("/")
    expect(page.locator('[data-test="inventory-container"]')).not_to_be_visible()










