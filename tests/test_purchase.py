from playwright.sync_api import sync_playwright

def test_purchase():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://www.saucedemo.com/")

        page.fill('input[name="user-name"]', 'standard_user')
        page.fill('input[name="password"]', 'secret_sauce')
        page.click('input[type="submit"]')

        page.click('text="Sauce Labs Backpack"')
        page.click('button[name="add-to-cart"]')

        page.click('a.shopping_cart_link')

        assert page.is_visible('text="Sauce Labs Backpack"')

        page.click('button[name="checkout"]')

        page.fill('input[name="firstName"]', 'John')
        page.fill('input[name="lastName"]', 'Doe')
        page.fill('input[name="postalCode"]', '12345')

        page.click('input[name="continue"]')

        page.click('button[name="finish"]')

        assert page.is_visible('text="Thank you for your order!"')

        browser.close()


if __name__ == "__main__":
    test_purchase()