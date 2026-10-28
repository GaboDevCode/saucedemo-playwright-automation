import pytest

from pages.login_page import LoginPage
from pages.InventoryPage import InventoryPage



@pytest.fixture

def logged_in_inventory(page) -> InventoryPage:

    login_page = LoginPage(page)
    login_page.navigate_to_login()
    login_page.login("standard_user", "secret_sauce")
    return  InventoryPage(page)


