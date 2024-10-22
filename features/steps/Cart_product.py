from behave import *
from pages.Cart_Page import CartProduct

use_step_matcher("re")


@given("User visit the home page")
def step_impl(context):
    context.cart_product = CartProduct(context.driver)


@step("User click on the desktop button")
def step_impl(context):
    context.cart_product.click_on_desktop()


@then("User click on the Mac button")
def step_impl(context):
    context.cart_product.click_on_mac()


@step("User click on the add to cart button")
def step_impl(context):
    context.cart_product.add_to_cart()


@then("User click on the home button")
def step_impl(context):
    context.cart_product.click_home_button()
