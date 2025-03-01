import time

import random

from features.PageObjects.Registration import Registration
from features.environment import *

from behave import *
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.ie.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager
number = random.randint(1000, 9999)
number1 = random.randint(1000, 9999)
new_email = "bdddemo" + str(number) + "@mailinator.com"
new_email1 = "bdddemo" + str(number1) + "@mailinator.com"


@given(u'I navigate to Register Page')
def step_impl(context):

    login_url = context.base_url
    context.driver.get(login_url)
    context.home = Registration(context.driver)
    time.sleep(2)
    context.home.my_account_click().click()
    context.home.register_click().click()
    time.sleep(2)


@when(u'I enter mandatory fields')
def step_impl(context):
    context.home.first_name().send_keys("ujjwal")
    context.home.last_name().send_keys("kumar")
    context.home.email().send_keys(new_email)
    time.sleep(2)
    context.home.phone_number().send_keys("1234567890")
    time.sleep(2)
    context.home.new_password().send_keys("Abcdef@123456")
    time.sleep(2)
    context.home.confirm_password().send_keys("Abcdef@123456")


@when(u'I select Privacy Policy Options')
def step_impl(context):
    context.home.privacy_policy().click()


@when(u'I click on Continue button')
def step_impl(context):
    context.home.continues().click()
    time.sleep(3)


@then(u'Account should get created')
def step_impl(context):
    time.sleep(3)
    assert context.home.registration().text== "Your Account Has Been Created!"


@when(u'I enter all fields')
def step_impl(context):
    context.home.first_name().send_keys("ujjwal")
    context.home.last_name().send_keys("kumar")
    context.home.email().send_keys(new_email1)
    time.sleep(2)
    context.home.phone_number().send_keys("1234567890")
    time.sleep(2)
    context.home.new_password().send_keys("Abcdef@123456")
    time.sleep(2)
    context.home.confirm_password().send_keys("Abcdef@123456")
    context.home.radio_button().click()
    time.sleep(3)


@when(u'I enter all fields except email address')
def step_impl(context):
    context.home.first_name().send_keys("ujjwal")
    context.home.last_name().send_keys("kumar")
    context.home.email().send_keys('')
    context.home.phone_number().send_keys("1234567890")
    context.home.new_password().send_keys("Abcdef@123456")
    context.home.confirm_password().send_keys("Abcdef@123456")
    context.home.radio_button().click()


@then(u'Proper warning message should be visible informing about missing of email field')
def step_impl(context):
    assert context.home.valid_email().text == 'E-Mail Address does not appear to be valid!'
    time.sleep(3)


@when(u'I enter existing email address into email fields')
def step_impl(context):
    context.home.first_name().send_keys("ujjwal")
    context.home.last_name().send_keys("kumar")
    context.home.email().send_keys("bdddemo2@mailinator.com")
    context.home.phone_number().send_keys("1234567890")
    context.home.new_password().send_keys("Abcdef@123456")
    context.home.confirm_password().send_keys("Abcdef@123456")
    context.home.radio_button().click()



@then(u'Proper warning message informing about duplicate account should be displayed.')
def step_impl(context):
    assert context.home.email_assert().text=='Warning: E-Mail Address is already registered!'
    time.sleep(3)


@when(u'I donot enter anything into the fields')
def step_impl(context):
    context.home.first_name().send_keys("")
    context.home.last_name().send_keys("")
    context.home.email().send_keys("")
    context.home.phone_number().send_keys("")
    context.home.new_password().send_keys("")
    context.home.confirm_password().send_keys("")



@then(u'Proper writing message for every mandatory fields should be displayed')
def step_impl(context):
    assert context.home.first_name_assert().text =='First Name must be between 1 and 32 characters!'
    assert context.home.last_name_assert().text == 'Last Name must be between 1 and 32 characters!'
    time.sleep(3)


