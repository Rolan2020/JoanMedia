# 1er test Playwright -> https://www.youtube.com/watch?v=Wka2DYrPCxQ
from playwright.sync_api import sync_playwright

# hacemos un with stament
# llamamos a la funcion sync_playwright() y la llamamos "p" -> la "p" va a estar utilizando los comandos de la libreria playwright
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    # metodo new_page
    page = browser.new_page()
    page.goto("http://whatsmyuseragent.org/")
    page.screenshot(path="demo.png")
    browser.close()