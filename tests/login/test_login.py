import pytest
from playwright.sync_api import Page, expect
from pages.login_page import LoginPage



USERNAME_REQUIRED_ERROR = "Epic sadface: Username is required"
PASSWORD_REQUIRED_ERROR = "Epic sadface: Password is required"
INVALID_CREDENTIALS_ERROR = ("Epic sadface: Username and password do not match any user in this service")


@pytest.mark.smoke
def test_login_valid_credentials(page: Page):
    """TC-LOGIN-001 | SC-LOGIN-001 | REQ-LOGIN-01"""
    login_page = LoginPage(page)
    login_page.navigate_to_login()
    login_page.login("standard_user", "secret_sauce")

    expect(page).to_have_url("/inventory.html")
    expect(page.locator('[data-test="inventory-container"]')).to_be_visible()



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
            "secret_sauce",
            id="TC-LOGIN-003-nonexistent_user_valid_password",
        ),
        pytest.param(
            "standard_user",
            "secret_user_demo",
            id="TC-LOGIN-004-valid_user_invalid_password",
        ),
    ],
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
@pytest.mark.parametrize(
    "username, password, expected_error",
    [
        pytest.param(
            "",
            "",
            USERNAME_REQUIRED_ERROR,
            id ="TC-LOGIN-005-login_empty_credentials",
        ),
         pytest.param(
            "standard_user",
             "",
            PASSWORD_REQUIRED_ERROR,
            id ="TC-LOGIN-006-login_valid_user_empty_password",
        ),
        pytest.param(
            "",
            "secret_sauce",
            USERNAME_REQUIRED_ERROR,
            id="TC-LOGIN-007-login_empty_user_valid_password",
        )
    ]
)
def test_login_credentials_required(page: Page, username: str, password: str, expected_error: str):
    """SC-LOGIN-005/006/007 | REQ-LOGIN-03"""
    login_page = LoginPage(page)
    login_page.navigate_to_login()
    login_page.login(username, password)

    expect(login_page.error_message).to_have_text(expected_error)
    expect(page).to_have_url("/")
    expect(page.locator('[data-test="inventory-container"]')).not_to_be_visible()
















