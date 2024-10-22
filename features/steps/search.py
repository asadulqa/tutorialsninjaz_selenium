from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.SerachProduct import SearchProduct

use_step_matcher("re")


@given("I got navigated to Home page")
def step_impl(context):
    context.search_product= SearchProduct(context.driver)
    expected_title = "Your Store"
    assert context.search_product.get_page_title(expected_title)


@when('I enter valid product say "HP" into the Search box field')
def step_impl(context):
    context.search_product.search_valid_product()


@step("I click on Search button")
def step_impl(context):
    context.search_product.click_on_search_button()


@then("Valid product should get displayed in Search results")
def step_impl(context):
    context.search_product.product_displayed()