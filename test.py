# tests/test_website.py
import asyncio
from playwright.async_api import Playwright, async_playwright, expect

# 替換成你要測試的網站 URL
WEBSITE_URL = "https://www.google.com" # 這裡請替換成你的實際網站 URL

async def run(playwright: Playwright):
    browser = await playwright.chromium.launch()
    page = await browser.new_page()
    await page.goto(WEBSITE_URL)

    # --- 檢查網站顯示是否正常的範例 ---

    # 範例 1: 檢查頁面標題是否正確
    await expect(page).to_have_title("Google") # 替換成你網站的預期標題

    # 範例 2: 檢查特定元素是否存在或可見
    # 例如：檢查一個 ID 為 'my-hero-section' 的元素是否可見
    # await expect(page.locator("#my-hero-section")).to_be_visible()

    # 範例 3: 檢查頁面內容是否包含特定文字
    # 例如：檢查頁面上是否有 'Welcome to our site!' 這些文字
    # await expect(page.locator("body")).to_contain_text("Google")

    # 範例 4: 截圖保存，方便除錯
    await page.screenshot(path="screenshot.png") # 截圖會保存到工作流程的 artifacts 中

    print(f"Successfully navigated to {WEBSITE_URL} and performed checks.")

    await browser.close()

async def main():
    async with async_playwright() as playwright:
        await run(playwright)

if __name__ == "__main_":
    asyncio.run(main())
