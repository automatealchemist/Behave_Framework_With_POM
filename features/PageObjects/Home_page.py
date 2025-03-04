import time

from selenium.webdriver.common.by import By

from utilities.Baseclass import Baseclass


class Desktop(Baseclass):
    def __init__(self,driver):
        super().__init__(driver)

    homepage_ele = (By.XPATH,'//*[@id="menu"]/div[2]/ul/li[1]/a')
    login_account = (By.XPATH, '//*[@id="content"]/h2[1]')

    def login_assert(self):
        assert self.driver.find_element(*Desktop.login_account).text == 'My Account'

    def homepage_element(self):

        self.driver.find_element(*Desktop.homepage_ele).click()
        time.sleep(3)


