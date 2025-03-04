from selenium.webdriver.common.by import By

from utilities.Baseclass import Baseclass


class Homepage(Baseclass):
    def __init__(self,driver):
        super().__init__(driver)

    my_account_xpath = (By.XPATH, '//*[@id="top-links"]/ul/li[2]/a')
    login_button_xpath = (By.XPATH, '//*[@id="top-links"]/ul/li[2]/ul/li[2]/a')
    email_id = (By.ID, 'input-email')
    password_id = (By.ID, 'input-password')
    input_submit_xpath = (By.XPATH, '//*[@id="content"]/div/div[2]/div/form/input')
    credential_missing_xpath = (By.XPATH,'//div[@class="alert alert-danger alert-dismissible"]')


    def my_account_click(self):
        self.click_on_element("my_account_xpath", '//*[@id="top-links"]/ul/li[2]/a')


    def login_click(self):
        self.click_on_element("login_button_xpath",'//*[@id="top-links"]/ul/li[2]/ul/li[2]/a')


    def input_submit_click(self):
        self.click_on_element(" input_submit_xpath",'//*[@id="content"]/div/div[2]/div/form/input')


    def valid_email(self,email):
        self.send_data("email_id",'input-email',email)


    def passwords(self,password):
        self.send_data("password_id", 'input-password', password)

    def invalid_password(self,password):
        self.send_data("password_id", 'input-password', password)


    def invalid_email(self,email):
        self.send_data("email_id", 'input-email', email)

    def blank_password(self,password):
        self.send_data("password_id", 'input-password', password)


    def blank_email(self,email):
        self.send_data("email_id", 'input-email', email)

    def credential_warning(self):
        assert self.driver.find_element(*Homepage.credential_missing_xpath).text== 'Warning: No match for E-Mail Address and/or Password.'






