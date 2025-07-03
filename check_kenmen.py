import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.kinmen.gov.tw/")
    page.get_by_role("link", name="機關介紹").first.click()
    page.locator("#base-content").get_by_role("link", name="連絡電話").click()
    expect(page.locator("tbody")).to_contain_text("單位電話")

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
