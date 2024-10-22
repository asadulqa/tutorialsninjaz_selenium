from selenium.webdriver.common.by import By
from pages.BasePage import BasePage
from locators import locator
from time import sleep


class CrateID(BasePage):

    def __init__(self,driver):
        super().__init__(driver)

    def click_account_button(self):
        account_button =(By.XPATH,locator.my_account_option_xpath)
        self.wait_for_element(account_button)
        self.click(account_button)

    def click_on_register_button(self):
        register_button = (By.LINK_TEXT,locator.register_option_link_text)
        self.wait_for_element_clickable(register_button)
        self.click(register_button)

    def enter_personal_info(self):
        first_name = (By.XPATH,locator.first_name_xpath)
        self.wait_for_element(first_name)
        self.click(first_name)
        self.send_keys(first_name,"Asadul")
        last_name = (By.XPATH,locator.last_name_xpath)
        self.wait_for_element(last_name)
        self.click(last_name)
        self.send_keys(last_name,"Haque")
        email = (By.XPATH,locator.email_xpath)
        self.wait_for_element(email)
        random_email = self.generate_random_email()
        self.send_keys(email,random_email)
        mobile =(By.XPATH,locator.telephone_xpath)
        self.wait_for_element(mobile)
        self.send_keys(mobile,"+8801346987598")

    def enter_password(self):
        password = (By.XPATH,locator.password_xpath)
        confirm_password = (By.XPATH,locator.confirm_password_xpath)
        self.click(password)
        self.send_keys(password,"123456789")
        self.click(confirm_password)
        self.send_keys(confirm_password, "123456789")

    def click_yes_button(self):
        yes_button = (By.XPATH,locator.newsletter_xpath)
        self.wait_for_element(yes_button)
        self.click(yes_button)

    def click_on_agree(self):
        agree = (By.XPATH,locator.agree_xpath)
        self.wait_for_element(agree)
        self.click(agree)

    def click_on_continue(self):
        continue_button = (By.XPATH,locator.continue_button_xpath)
        self.wait_for_element(continue_button)
        self.click(continue_button)

    def verify_account_create(self):
        verify = (By.LINK_TEXT,locator.home_page_link_text)
        get_t = self.get_text(verify)
        assert get_t == 'Qafox.com'


    def click_on_logout(self):
        logout =(By.LINK_TEXT,locator.logout_link_text)
        self.wait_for_element(logout)
        self.click(logout)

    def logout_done(self):
        element = (By.LINK_TEXT,locator.continue_link_text)
        self.click(element)

    def click_on_login(self):
        login = (By.LINK_TEXT,locator.login_option_link_text)
        self.wait_for_element(login)
        self.click(login)

    def input_credential(self):
        email = (By.XPATH,locator.email_xpath)
        password = (By.XPATH,locator.password_xpath)
        self.wait_for_element(email)
        self.send_keys(email,"mdasadul@gmail.com")
        self.wait_for_element(password)
        self.send_keys(password, "12345678")

    def verify_login_successful(self):
        login = (By.XPATH, locator.login_xpath)
        self.wait_for_element(login)
        self.click(login)
        successful_status = (By.XPATH,locator.done_status)
        get_text = self.get_text(successful_status)
        assert get_text == "My Account"




