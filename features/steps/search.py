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
    #chrome_option = Options()
    #chrome_option.add_experimental_option("detach", True)
    #context.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_option)
    #context.driver.maximize_window()'''
    context.driver.get("https://tutorialsninja.com/demo/")



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
   # context.driver.quit()



@when(u'I enter invalid product name in search box field')
def step_impl(context):
    context.driver.find_element(By.NAME, 'search').send_keys("abcxz")



@then(u'proper message should be visible in the search result')
def step_impl(context):
    time.sleep(3)
   #assert context.driver.find_element(By.XPATH,'//*[@id="content"]/p[2]').text =="There is no product that matches the search criteria."
    sample_text ="There is no product that matches the search criteria."
    assert context.driver.find_element(By.XPATH,
                                       '//*[@id="content"]/p[2]').text.__eq__(sample_text)
 #   context.driver.quit()



@when(u'I donot enter anything in the search box field')
def step_impl(context):
    time.sleep(3)
    context.driver.find_element(By.XPATH, '//*[@id="search"]/span/button').click()



