import time

from behave import *
import selenium
from behave import *
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.ie.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager
from features.environment import *

@given(u'I navigated to Login page')
def step_impl(context):
    login_url = context.base_url + "demo/index.php?route=account/login"
    context.driver.get(login_url)
    time.sleep(4)


@when(u'I enter valid email address and password')
def step_impl(context):
    context.driver.find_element(By.ID,'input-email').send_keys('amotooriapril2023@gmail.com')
    time.sleep(3)
    context.driver.find_element(By.ID,'input-password').send_keys('12345')


@when(u'I click on the Login Button')
def step_impl(context):
    context.driver.find_element(By.XPATH,'//*[@id="content"]/div/div[2]/div/form/input').click()


@then(u'I should logged in')
def step_impl(context):
    assert context.driver.current_url == 'https://tutorialsninja.com/demo/index.php?route=account/account'


@when(u'I enter invalid email address and valid password')
def step_impl(context):
    context.driver.find_element(By.ID, 'input-email').send_keys('motooriapril2023@gmail.com')
    context.driver.find_element(By.ID, 'input-password').send_keys('12345')


@then(u'I should get a proper warning message')
def step_impl(context):
    assert context.driver.find_element(By.XPATH,'//div[@class="alert alert-danger alert-dismissible"]').text == 'Warning: No match for E-Mail Address and/or Password.'


@when(u'I enter valid email address and invalid password')
def step_impl(context):
    context.driver.find_element(By.ID, 'input-email').send_keys('amotooriapril2023@gmail.com')
    context.driver.find_element(By.ID, 'input-password').send_keys('02345')


@when(u'I enter invalid email address and invalid password')
def step_impl(context):
    context.driver.find_element(By.ID, 'input-email').send_keys('motooriapril2023@gmail.com')
    context.driver.find_element(By.ID, 'input-password').send_keys('62345')


@when(u'I donot enter anything into email address and invalid password')
def step_impl(context):
    context.driver.find_element(By.ID, 'input-email').send_keys('')
    context.driver.find_element(By.ID, 'input-password').send_keys('')
