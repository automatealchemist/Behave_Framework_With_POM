
from features.environment import *
from features.PageObjects.Login import *


import time
from features.PageObjects.Login import Homepage
from behave import given, when

class Features:
    @given(u'I navigated to Login page')
    def step_impl(context):
        login_url = context.base_url
        context.driver.get(login_url)
        context.home = Homepage(context.driver)
        time.sleep(2)
        context.home.my_account_click().click()
        context.home.login_click().click()

    @when(u'I enter valid email address and password')
    def step_impl(context):
        time.sleep(3)
        context.home.valid_email()
        time.sleep(3)
        context.home.passwords()



    @when(u'I click on the Login Button')
    def step_impl(context):
        context.home.input_submit_click().click()
        time.sleep(3)


    @then(u'I should logged in')
    def step_impl(context):
        assert context.driver.current_url == 'https://tutorialsninja.com/demo/index.php?route=account/account'


    @when(u'I enter invalid email address and valid password')
    def step_impl(context):
        context.home.invalid_email()
        context.home.passwords()


    @then(u'I should get a proper warning message')
    def step_impl(context):
        assert context.driver.find_element(By.XPATH,
                                       '//div[@class="alert alert-danger alert-dismissible"]').text == 'Warning: No match for E-Mail Address and/or Password.'


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
