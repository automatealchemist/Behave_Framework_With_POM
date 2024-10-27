import time

import random



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
    chrome_option = Options()
    chrome_option.add_experimental_option("detach", True)
    context.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_option)
    context.driver.maximize_window()
    context.driver.get("https://tutorialsninja.com/demo/index.php?route=account/register")
    # raise NotImplementedError(u'STEP: Given I navigate to Register Page')


@when(u'I enter mandatory fields')
def step_impl(context):
    context.driver.find_element(By.ID,'input-firstname').send_keys("ujjwal")
    context.driver.find_element(By.ID, 'input-lastname').send_keys("kumar")
    context.driver.find_element(By.ID, 'input-email').send_keys(new_email)
    context.driver.find_element(By.ID, 'input-telephone').send_keys("1234567890")
    context.driver.find_element(By.ID, 'input-password').send_keys("Abcdef@123456")
    context.driver.find_element(By.ID, 'input-confirm').send_keys("Abcdef@123456")


@when(u'I select Privacy Policy Options')
def step_impl(context):
    context.driver.find_element(By.XPATH,'//*[@id="content"]/form/div/div/input[1]').click()


@when(u'I click on Continue button')
def step_impl(context):
    context.driver.find_element(By.XPATH,'//*[@id="content"]/form/div/div/input[2]').click()
  #  raise NotImplementedError(u'STEP: When I click on Continue button')


@then(u'Account should get created')
def step_impl(context):
    assert context.driver.current_url =='https://tutorialsninja.com/demo/index.php?route=account/success'
    context.driver.quit()


@when(u'I enter all fields')
def step_impl(context):
    context.driver.find_element(By.ID,'input-firstname').send_keys("ujjwal")
    context.driver.find_element(By.ID, 'input-lastname').send_keys("kumar")
    context.driver.find_element(By.ID, 'input-email').send_keys(new_email1)
    context.driver.find_element(By.ID, 'input-telephone').send_keys("1234567890")
    context.driver.find_element(By.ID, 'input-password').send_keys("Abcdef@123456")
    context.driver.find_element(By.ID, 'input-confirm').send_keys("Abcdef@123456")
    context.driver.find_element(By.XPATH,'//*[@id="content"]/form/fieldset[3]/div/div/label[1]').click()


@when(u'I enter all fields except email address')
def step_impl(context):
    context.driver.find_element(By.ID, 'input-firstname').send_keys("ujjwal")
    context.driver.find_element(By.ID, 'input-lastname').send_keys("kumar")
    context.driver.find_element(By.ID, 'input-email').send_keys('')
    context.driver.find_element(By.ID, 'input-telephone').send_keys("1234567890")
    context.driver.find_element(By.ID, 'input-password').send_keys("Abcdef@123456")
    context.driver.find_element(By.ID, 'input-confirm').send_keys("Abcdef@123456")
    context.driver.find_element(By.XPATH, '//*[@id="content"]/form/fieldset[3]/div/div/label[1]').click()
   # raise NotImplementedError(u'STEP: When I enter details into all fields except email field')

@then(u'Proper warning message should be visible informing about missing of email field')
def step_impl(context):
    assert context.driver.find_element(By.XPATH,'//*[@id="account"]/div[4]/div/div').text == 'E-Mail Address does not appear to be valid!'
    time.sleep(3)
    context.driver.quit()

@when(u'I enter existing email address into email fields')
def step_impl(context):
    context.driver.find_element(By.ID,'input-firstname').send_keys("ujjwal")
    context.driver.find_element(By.ID, 'input-lastname').send_keys("kumar")
    context.driver.find_element(By.ID, 'input-email').send_keys("bdddemo2@mailinator.com")
    context.driver.find_element(By.ID, 'input-telephone').send_keys("1234567890")
    context.driver.find_element(By.ID, 'input-password').send_keys("Abcdef@123456")
    context.driver.find_element(By.ID, 'input-confirm').send_keys("Abcdef@123456")
    context.driver.find_element(By.XPATH,'//*[@id="content"]/form/fieldset[3]/div/div/label[1]').click()
  #  raise NotImplementedError(u'STEP: When I enter existing email address into email fields')


@then(u'Proper warning message informing about duplicate account should be displayed.')
def step_impl(context):
    assert context.driver.find_element(By.XPATH,"//div[@class='alert alert-danger alert-dismissible']").text=='Warning: E-Mail Address is already registered!'
    time.sleep(3)
    context.driver.quit()
 #   raise NotImplementedError(u'STEP: Then Proper warning message informing about duplicate account should be displayed.')

'''
@given(u'I navigate to Register page')
def step_impl(context):
    pass
 #   raise NotImplementedError(u'STEP: Given I navigate to Register page')
'''

@when(u'I donot enter anything into the fields')
def step_impl(context):
    context.driver.find_element(By.ID, 'input-firstname').send_keys("")
    context.driver.find_element(By.ID, 'input-lastname').send_keys("")
    context.driver.find_element(By.ID, 'input-email').send_keys("")
    context.driver.find_element(By.ID, 'input-telephone').send_keys("")
    context.driver.find_element(By.ID, 'input-password').send_keys("")
    context.driver.find_element(By.ID, 'input-confirm').send_keys("")
  #  raise NotImplementedError(u'STEP: When I donot enter anything into the fields')


@when(u'I click on the Continue button')
def step_impl(context):
    context.driver.find_element(By.XPATH,'//*[@id="content"]/form/div/div/input[2]').click()
 #   raise NotImplementedError(u'STEP: When I click on the Continue button')


@then(u'Proper writing message for every mandatory fields should be displayed')
def step_impl(context):
    assert context.driver.find_element(By.XPATH,'//*[@id="account"]/div[2]/div/div').text =='First Name must be between 1 and 32 characters!'
    time.sleep(3)
    context.driver.quit()
 #   raise NotImplementedError(u'STEP: Then Proper writing message for every mandatory fields should be displayed')
