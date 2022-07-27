from playwright.sync_api import Page
import pytest

# @pytest.mark.only_browser("chromium")
def test_title(page : Page):
    page.goto("https://www.saucedemo.com/")
    #page.goto("/")
    assert page.title() == "Swag Labs"

# @pytest.mark.skip_browser("chromium")
def test_inventory_page(page : Page):
    page.goto("https://www.saucedemo.com/inventory.html")
    #page.goto("/inventory.html")
    assert page.inner_text("h3") == "Epic sadface: You can only access '/inventory.html' when you are logged in."

# con el comando --browser-channel chrome, el test se queda frizeado