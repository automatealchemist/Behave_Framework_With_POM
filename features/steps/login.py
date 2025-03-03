from features.environment import *
from features.PageObjects.Login import *
import time
from features.PageObjects.Login import Homepage
from behave import given, when
from features.PageObjects.Home_page import Desktop


class Features:
    @given(u'I navigated to Login page')
    def step_impl(context):
        context.driver.get(context.base_url)
        context.home = Homepage(context.driver)
        time.sleep(2)
        context.home.my_account_click()
        context.home.login_click()

    @when(u'I enter valid email address and password')
    def step_impl(context):
        time.sleep(3)
        context.home.valid_email()
        time.sleep(3)
        context.home.passwords()



    @when(u'I click on the Login Button')
    def step_impl(context):
        context.home.input_submit_click()
        time.sleep(3)


    @then(u'I should logged in')
    def step_impl(context):
        context.desktop = Desktop(context.driver)
        context.desktop.login_assert()

    @then(u'I click on Desktop')
    def step_impl(context):
        context.desktop = Desktop(context.driver)
        context.desktop.homepage_element()

    @when(u'I enter invalid email address and valid password')
    def step_impl(context):
        context.home.invalid_email()
        context.home.passwords()


    @then(u'I should get a proper warning message')
    def step_impl(context):
        context.home.credential_warning()


    @when(u'I enter valid email address and invalid password')
    def step_impl(context):
        context.home.valid_email()
        context.home.inavlid_password()


    @when(u'I enter invalid email address and invalid password')
    def step_impl(context):
        context.home.invalid_email()
        context.home.inavlid_password()


    @when(u'I donot enter anything into email address and invalid password')
    def step_impl(context):
        context.home.blank_email()
        context.home.blank_password()
