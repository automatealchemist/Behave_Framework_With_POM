from selenium.webdriver.common.by import By


class Homepage:
    def __init__(self, driver):
        self.driver = driver

    my_account = (By.XPATH, '//*[@id="top-links"]/ul/li[2]/a')
    login_button = (By.XPATH, '//*[@id="top-links"]/ul/li[2]/ul/li[2]/a')
    email = (By.ID, 'input-email')
    password = (By.ID, 'input-password')
    input_submit = (By.XPATH, '//*[@id="content"]/div/div[2]/div/form/input')

    def my_account_click(self):
        return self.driver.find_element(*Homepage.my_account)

    def login_click(self):
        return self.driver.find_element(*Homepage.login_button)

    def input_submit_click(self):
        return self.driver.find_element(*Homepage.input_submit)

    def valid_email(self):
        self.driver.find_element(*Homepage.email).send_keys('amotooriapril2023@gmail.com')

    def passwords(self):
        self.driver.find_element(*Homepage.password).send_keys('12345')

    def inavlid_password(self):
        self.driver.find_element(*Homepage.password).send_keys('02345')

    def invalid_email(self):
        self.driver.find_element(*Homepage.email).send_keys('motooriapril2023@gmail.com')

    def blank_password(self):
        self.driver.find_element(*Homepage.password).send_keys('')

    def blank_email(self):
        self.driver.find_element(*Homepage.email).send_keys('')




