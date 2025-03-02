import time
from itertools import dropwhile

import selenium
from behave import *


from features.PageObjects.Search import Search


@given(u'I got navigated to Homepage')
def step_impl(context):
    search_url = context.base_url
    context.driver.get(search_url)
    context.home = Search(context.driver)

@when(u'I enter valid product name in search box field')
def step_impl(context):
    time.sleep(3)
    context.home.search_valid_keyword()

@when(u'I click on the search button')
def step_impl(context):
    context.home.search_button()

@then(u'Valid product should be visible in the search result')
def step_impl(context):
    context.home.search_result()

@when(u'I enter invalid product name in search box field')
def step_impl(context):
    context.home.search_invalid_keyword()

@then(u'proper message should be visible in the search result')
def step_impl(context):
    time.sleep(3)
    context.home.search_text()

@when(u'I donot enter anything in the search box field')
def step_impl(context):
    time.sleep(3)
    context.home.search_button()



