from selenium.webdriver.common.by import By
from locators import locator
from time import sleep
from pages.BasePage import BasePage


class SearchProduct(BasePage):
    def __init__(self,driver):
        super().__init__(driver)

    def get_page_title(self,expected_title):
        return self.driver.title.__eq__(expected_title)

    def search_valid_product(self):
        valid_product =(By.XPATH,locator.search_box_field_name)
        self.wait_for_element(valid_product)
        self.click(valid_product)
        self.send_keys(valid_product,"HP")


    def click_on_search_button(self):
        click_search = (By.XPATH,locator.search_button_xpath)
        self.wait_for_element(click_search)
        self.click(click_search)

    def product_displayed(self):
        product_displayed = (By.LINK_TEXT,locator.product_option_link_text)
        self.wait_for_element(product_displayed)
        return self.driver.find_element(By.LINK_TEXT,locator.product_option_link_text).is_displayed()

