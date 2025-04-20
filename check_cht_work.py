import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://rmis.cht.com.tw/portal/jobs/joblist.jsp")
    expect(page.locator("section")).to_contain_text("寬頻電路及用戶終端設備管理")


    work_name = page.locator(".cht-jobcard-h5.cht-text-2lines")
    count = work_name.count()
    print("Work Name Count:", count)

    for i in range(count):
        text = work_name.nth(i).inner_text()
        if '機房' in text:
            print("Found:", text)

    print('hello')

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
