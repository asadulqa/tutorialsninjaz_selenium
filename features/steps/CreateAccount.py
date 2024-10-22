from behave import *
from pages.CreateID import CrateID

use_step_matcher("re")


@given("I got Home page")
def step_impl(context):
    context.create_id = CrateID(context.driver)


@then("User click on the Account button")
def step_impl(context):
    context.create_id.click_account_button()


@step("User click on the Register button")
def step_impl(context):
    context.create_id.click_on_register_button()


@then("User Enter Your Personal Details")
def step_impl(context):
    context.create_id.enter_personal_info()


@step("User Enter strong Password")
def step_impl(context):
    context.create_id.enter_password()


@step("User click on the Newsletter 'Yes' button")
def step_impl(context):
    context.create_id.click_yes_button()


@then("User click on the agree button")
def step_impl(context):
    context.create_id.click_on_agree()


@then("User click on the continue")
def step_impl(context):
    context.create_id.click_on_continue()


@step("User verify the account create successful")
def step_impl(context):
    context.create_id.verify_account_create()


@then("User Logout the create account")
def step_impl(context):
    context.create_id.click_on_logout()


@then("User click continue")
def step_impl(context):
    context.create_id.logout_done()


@step("User click on the Login button")
def step_impl(context):
    context.create_id.click_on_login()


@then("User Enter the Email and Password")
def step_impl(context):
    context.create_id.input_credential()


@step("User Verify the Login successful")
def step_impl(context):
    context.create_id.click_on_login()