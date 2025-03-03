from features.PageObjects.Registration import Registration
from features.environment import *
from behave import *


@given(u'I navigate to Register Page')
def step_impl(context):

    context.driver.get(context.base_url)
    context.home = Registration(context.driver)
    time.sleep(2)
    context.home.my_account_click()
    context.home.register_click()
    time.sleep(2)


@when(u'I enter mandatory fields')
def step_impl(context):
    context.home.first_name()
    context.home.last_name()
    context.home.email()
    time.sleep(2)
    context.home.phone_number()
    time.sleep(2)
    context.home.new_password()
    time.sleep(2)
    context.home.confirm_password()


@when(u'I select Privacy Policy Options')
def step_impl(context):
    context.home.privacy_policy()


@when(u'I click on Continue button')
def step_impl(context):
    context.home.continues()
    time.sleep(3)


@then(u'Account should get created')
def step_impl(context):
    time.sleep(3)
    context.home.assert_registration()


@when(u'I enter all fields')
def step_impl(context):
    context.home.first_name()
    context.home.last_name()
    context.home.email_1()
    time.sleep(2)
    context.home.phone_number()
    time.sleep(2)
    context.home.new_password()
    time.sleep(2)
    context.home.confirm_password()
    context.home.radio_button()
    time.sleep(3)


@when(u'I enter all fields except email address')
def step_impl(context):
    context.home.first_name()
    context.home.last_name()
    context.home.email_blank()
    context.home.phone_number()
    context.home.new_password()
    context.home.confirm_password()
    context.home.radio_button()


@then(u'Proper warning message should be visible informing about missing of email field')
def step_impl(context):
    context.home.email_assert()
    time.sleep(3)


@when(u'I enter existing email address into email fields')
def step_impl(context):
    context.home.first_name()
    context.home.last_name()
    context.home.email()
    context.home.phone_number()
    context.home.new_password()
    context.home.confirm_password()
    context.home.radio_button()



@then(u'Proper warning message informing about duplicate account should be displayed.')
def step_impl(context):
    context.home.email_duplicate()
    time.sleep(3)


@when(u'I donot enter anything into the fields')
def step_impl(context):
    context.home.first_name_blank()
    context.home.last_name_blank()
    context.home.email_blank()
    context.home.phone_number_blank()
    context.home.new_password_blank()
    context.home.confirm_password_blank()



@then(u'Proper writing message for every mandatory fields should be displayed')
def step_impl(context):
    context.home.fields_assert()

    time.sleep(3)


