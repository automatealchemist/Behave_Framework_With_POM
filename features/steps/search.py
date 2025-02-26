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


@given(u'I got navigated to Homepage')
def step_impl(context):
    search_url = context.base_url+"demo"
    context.driver.get(search_url)

@when(u'I enter valid product name in search box field')
def step_impl(context):
    time.sleep(3)
    context.driver.find_element(By.NAME, 'search').send_keys("HP")

@when(u'I click on the search button')
def step_impl(context):
    context.driver.find_element(By.XPATH, '//*[@id="search"]/span/button').click()

@then(u'Valid product should be visible in the search result')
def step_impl(context):
    assert context.driver.find_element(By.LINK_TEXT,"HP LP3065").is_displayed()
    context.driver.find_element(By.LINK_TEXT,"HP LP3065").click()

@when(u'I enter invalid product name in search box field')
def step_impl(context):
    context.driver.find_element(By.NAME, 'search').send_keys("abcxz")

@then(u'proper message should be visible in the search result')
def step_impl(context):
    time.sleep(3)
    sample_text ="There is no product that matches the search criteria."
    assert context.driver.find_element(By.XPATH, '//*[@id="content"]/p[2]').text.__eq__(sample_text)

@when(u'I donot enter anything in the search box field')
def step_impl(context):
    time.sleep(3)
    context.driver.find_element(By.XPATH, '//*[@id="search"]/span/button').click()



