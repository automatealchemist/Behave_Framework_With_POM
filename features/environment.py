
import time
import random

import allure
from allure_commons.types import AttachmentType
from behave import *
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.ie.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager
from win32pdhutil import browse
from utilities import *
from utilities import ConfigReader


def before_scenario(context,scenario):
    browser_name = ConfigReader.read_configuration("basic info","browser")
    if browser_name =="chrome":
        chrome_option = Options()
        chrome_option.add_experimental_option("detach", True)
        context.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_option)
        context.driver.maximize_window()
    else:
        print("Invalid browser name")

    context.base_url = ConfigReader.read_configuration("basic info", "url").strip()
    context.driver.get(context.base_url)


def after_scenario(context,scenario):
    context.driver.quit()

def after_step(context,step):
    if step.status =='failed':
        allure.attach(context.driver.get_screenshot_as_png(),name ="failed_screenshot",attachment_type=AttachmentType.PNG)