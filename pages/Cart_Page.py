from selenium.webdriver.common.by import By
from pages.BasePage import BasePage
from locators import locator

class CartProduct(BasePage):

    def __init__(self,driver):
        super().__init__(driver)

    def click_on_desktop(self):
        click_element = (By.LINK_TEXT,locator.desktop_link_text)
        self.wait_for_element(click_element)
        self.click(click_element)


    def click_on_mac(self):
        click_mac =(By.LINK_TEXT,locator.mac_link_text)
        self.wait_for_element(click_mac)
        self.click(click_mac)


    def add_to_cart(self):
        cart_element = (By.XPATH,locator.cart_button)
        self.wait_for_element(cart_element)
        self.click(cart_element)


    def click_home_button(self):
        home_button = (By.LINK_TEXT,locator.home_page_link_text)
        self.wait_for_element(home_button)
        self.click(home_button)








