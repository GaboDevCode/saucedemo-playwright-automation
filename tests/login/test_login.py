import pytest
from playwright.sync_api import Page, expect
from pages.login_page import LoginPage



USERNAME_REQUIRED_ERROR = "Epic sadface: Username is required"
PASSWORD_REQUIRED_ERROR = "Epic sadface: Password is required"
INVALID_CREDENTIALS_ERROR = ("Epic sadface: Username and password do not match any user in this service")
USER_BLOCKED_ERROR = "Epic sadface: Sorry, this user has been locked out."





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
        ),
        pytest.param(
            "locked_out_user",
            "secret_sauce",
            USER_BLOCKED_ERROR,
            id="TC-LOGIN-008-login_locked_out_user"
            ,
        )
    ]
)
def test_login_rejected(page: Page, username: str, password: str, expected_error: str):
    """SC-LOGIN-005/006/007 | REQ-LOGIN-03 · SC-LOGIN-008 | REQ-LOGIN-04"""
    login_page = LoginPage(page)
    login_page.navigate_to_login()
    login_page.login(username, password)

    expect(login_page.error_message).to_have_text(expected_error)
    expect(page).to_have_url("/")
    expect(page.locator('[data-test="inventory-container"]')).not_to_be_visible()




@pytest.mark.regression
@pytest.mark.parametrize(
    "path, expected_error",
    [
        pytest.param(
    "/inventory.html",
            "Epic sadface: You can only access '/inventory.html' when you are logged in.",
            id="TC-LOGIN-009-inventory"
        ),
        pytest.param(
        "/cart.html",
                "Epic sadface: You can only access '/cart.html' when you are logged in.",
         id="TC-LOGIN-009-Cart"
       ),
        pytest.param(
    "/checkout-step-one.html",
            "Epic sadface: You can only access '/checkout-step-one.html' when you are logged in.",
        id="TC-LOGIN-009-checkout_step_one"
    ),
  ]
)


def test_access_internal_page_without_session(page: Page, path: str, expected_error: str):
    """SC-LOGIN-009 | REQ-LOGIN-05"""

    login_page = LoginPage(page)
    page.goto(path)

    expect(page).to_have_url("/")
    expect(login_page.error_message).to_have_text(expected_error)
    expect(page.locator('[data-test="inventory-container"]')).not_to_be_visible()















