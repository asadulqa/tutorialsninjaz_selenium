import random
import string
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By

class BasePage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.timeout = timeout


    def find_element(self, locator):
        return WebDriverWait(self.driver, self.timeout).until(
            EC.presence_of_element_located(locator)
        )


    def find_elements(self, locator):
        return WebDriverWait(self.driver, self.timeout).until(
            EC.presence_of_all_elements_located(locator)
        )


    def click(self, locator):
        element = self.find_element(locator)
        element.click()


    def send_keys(self, locator, text):
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)


    def wait_for_element_visible(self, locator):
        return WebDriverWait(self.driver, self.timeout).until(
            EC.visibility_of_element_located(locator)
        )


    def is_element_present(self, locator):
        try:
            self.find_element(locator)
            return True
        except TimeoutException:
            return False


    def hover(self, locator, wait_seconds=2):
        element = self.find_element(locator)
        action_obj = ActionChains(self.driver)
        action_obj.move_to_element(element)
        action_obj.perform()


    def wait_for_element(self,locator,timeout=10):
        WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    def wait_for_page_loaded(self, timeout=120):
        WebDriverWait(self.driver, timeout).until(PageLoaded())

    def wait_for_element_clickable(self, locator):
        try:
            return WebDriverWait(self.driver, self.timeout).until(
                EC.element_to_be_clickable(locator)
            )
        except TimeoutException:
            print(f"Element with locator {locator} was not clickable within {self.timeout} seconds")
            return None


    def double_click(self, locator):
        source = self.find_element(locator)
        action = ActionChains(self.driver)
        action.double_click(source).perform()

    def switch_to_new_window(self, win_handle):
        self.driver.switch_to.window(win_handle)

    def refresh_browser(self):
        self.driver.refresh()

    def get_window_handles(self):
        return self.driver.window_handles


    def get_current_window_handle(self):
        return self.driver.current_window_handle

    def switch_control_to_app(self):
        try:
            self.driver.switch_to.context('NATIVE_APP')
        except Exception as e:
            raise Exception("Unable to switch control to app")

    def get_title(self):
        return self.driver.title

    def get_text(self, locator):
        element = self.find_element(locator)
        return element.text

    def back(self):
        self.driver.back()

    def maximize_browser(self):
        self.driver.maximize_window()

    def close_browser(self):
        self.driver.close()

    def generate_random_email(self, prefix="user", domain="example.com"):
        random_part = ''.join(random.choices(string.ascii_lowercase + string.digits, k=5))
        return f"{prefix}{random_part}@{domain}"




class PageLoaded:
    def __call__(self, dr):
        ready = dr.execute_script(
            "return document.readyState=='complete';"
        )
        if ready:
            return True
        else:
            return False