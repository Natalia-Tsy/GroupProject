from pages.locators import LoginPageLocators, ProductPageLocators, YourCartPage
from pages.locators import YourInfoPageLocators, CheckoutOverviewLocators, CheckoutCompleteLocators
import conf


class TestPlaceOrder:
    def test_place_order(self, d):
        assert d.current_url == conf.URL

        # login
        d.find_element(*LoginPageLocators.LOGIN_FORM).send_keys("standard_user")
        d.find_element(*LoginPageLocators.PASSWORD_FORM).send_keys("secret_sauce")
        d.find_element(*LoginPageLocators.LOGIN_BUTTON).click()

        assert d.title == 'Swag Labs', 'Wrong title'
        assert d.current_url == "https://www.saucedemo.com/inventory.html"

        d.find_element(*ProductPageLocators.SAUCE_LABS_BACKPACK_ADD_TO_CART).click()
        d.find_element(*ProductPageLocators.SHOPPING_CART_LINK).click()

        d.find_element(*YourCartPage.CHECKOUT_BUTTON).click()

        d.find_element(*YourInfoPageLocators.YOUR_FIRST_NAME).send_keys("John")
        d.find_element(*YourInfoPageLocators.YOUR_LAST_NAME).send_keys("Smith")
        d.find_element(*YourInfoPageLocators.YOUR_ZIP).send_keys("33009")
        d.find_element(*YourInfoPageLocators.YOUR_CONTINUE).click()

        assert d.current_url == "https://www.saucedemo.com/checkout-step-two.html"
        qty_label = d.find_element(*CheckoutOverviewLocators.QUANTITY_LABEL)
        desc_label = d.find_element(*CheckoutOverviewLocators.DESCRIPTION_LABEL)
        assert qty_label.text == "QTY"
        assert desc_label.text == "DESCRIPTION"
        d.find_element(*CheckoutOverviewLocators.FINISH_BUTTON).click()

        assert d.current_url == "https://www.saucedemo.com/checkout-complete.html"
        header_message = d.find_element(*CheckoutCompleteLocators.HEADER_MESSAGE)
        text_message = d.find_element(*CheckoutCompleteLocators.TEXT_MESSAGE)
        assert header_message.text == "THANK YOU FOR YOUR ORDER"
        assert text_message.text == "Your order has been dispatched, and will arrive just as fast as the pony can get there!"
