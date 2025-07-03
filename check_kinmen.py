# tests/test_kinmen_website.py
import pytest
from playwright.sync_api import Page, expect

# 替換成你要測試的網站 URL
WEBSITE_URL = "https://www.kinmen.gov.tw/"

@pytest.fixture(scope="function", autouse=True)
def browser_page(playwright_browser):
    # 使用 pytest-playwright 提供的 browser fixture
    page = playwright_browser.new_page()
    yield page
    # 在測試結束後關閉頁面，這樣截圖就會在測試失敗時被保存
    page.close()

def test_kinmen_contact_info(browser_page: Page):
    page = browser_page
    screenshot_path = "screenshot_final.png" # 統一一個截圖檔名，或者區分成功/失敗

    try:
        page.goto(WEBSITE_URL)
        page.get_by_role("link", name="機關介紹").first.click()
        expect(page.locator("tbody")).to_contain_text("單位電話")
        print("Test passed: '單位電話' found in tbody.")
        # 如果測試成功，也在這裡截圖
        page.screenshot(path=screenshot_path)
    except AssertionError as e:
        print(f"Test failed: {e}")
        page.screenshot(path=screenshot_path) # 失敗時截圖
        pytest.fail(f"Test failed and screenshot taken: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        page.screenshot(path=screenshot_path) # 意外錯誤時截圖
        pytest.fail(f"Unexpected error and screenshot taken: {e}")
    finally:
        # 確保在任何情況下都嘗試截圖 (但要避免重複截圖)
        # 更好的做法是，確保你的截圖邏輯在測試結果無論如何都執行到
        pass # 在這個修改版中，try/except 已經處理了截圖