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
    screenshot_path = "screenshot_error.png" # 設定截圖的路徑

    try:
        page.goto(WEBSITE_URL)
        page.get_by_role("link", name="機關介紹").first.click()

        # 執行你的檢查
        expect(page.locator("tbody")).to_contain_text("單位電話")
        print("Test passed: '單位電話' found in tbody.")

    except AssertionError as e:
        # 如果斷言失敗，截圖並重新拋出錯誤
        print(f"Test failed: {e}")
        page.screenshot(path=screenshot_path)
        pytest.fail(f"Test failed and screenshot taken: {e}")
    except Exception as e:
        # 其他任何錯誤，也截圖
        print(f"An unexpected error occurred: {e}")
        page.screenshot(path=screenshot_path)
        pytest.fail(f"Unexpected error and screenshot taken: {e}")

    finally:
        # 即使成功，也可以考慮截圖，以便於確認正常顯示
        # 如果你只想要失敗才截圖，可以將此行移到 except 區塊中
        if not pytest.current_test_status == "passed": # 如果測試不是通過狀態
             page.screenshot(path=screenshot_path) # 再確保截圖一次 (避免斷言外錯誤)