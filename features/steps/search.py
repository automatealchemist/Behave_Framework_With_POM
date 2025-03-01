import time
from itertools import dropwhile

import selenium
from behave import *
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.ie.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager

from features.PageObjects.Search import Search


@given(u'I got navigated to Homepage')
def step_impl(context):
    search_url = context.base_url
    context.driver.get(search_url)
    context.home = Search(context.driver)

@when(u'I enter valid product name in search box field')
def step_impl(context):
    time.sleep(3)
    context.home.search_keyword().send_keys("HP")

@when(u'I click on the search button')
def step_impl(context):
    context.home.search_button().click()

@then(u'Valid product should be visible in the search result')
def step_impl(context):
    assert context.home.search_result().is_displayed()
    context.home.search_result().click()

@when(u'I enter invalid product name in search box field')
def step_impl(context):
    context.home.search_keyword().send_keys("abcxz")

@then(u'proper message should be visible in the search result')
def step_impl(context):
    time.sleep(3)
    sample_text ="There is no product that matches the search criteria."
    assert context.home.search_text().text.__eq__(sample_text)

@when(u'I donot enter anything in the search box field')
def step_impl(context):
    time.sleep(3)
    context.home.search_button().click()



