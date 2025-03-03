import random

from selenium.webdriver.common.by import By

from features.PageObjects.Baseclass import Baseclass

number = random.randint(1000, 9999)
number1 = random.randint(1000, 9999)
new_email = "bdddemo" + str(number) + "@mailinator.com"
new_email1 = "bdddemo" + str(number1) + "@mailinator.com"

class Registration(Baseclass):

    def __init__(self,driver):
        super().__init__(driver)


    my_account = (By.XPATH, '//*[@id="top-links"]/ul/li[2]/a')
    register_button = (By.XPATH, '//*[@id="top-links"]/ul/li[2]/ul/li[1]/a')
    firstname=(By.ID,'input-firstname')
    lastname=(By.ID, 'input-lastname')
    emails= (By.ID, 'input-email')
    mobilenumber =(By.ID, 'input-telephone')
    newpassword = (By.ID, 'input-password')
    confirmpassword =(By.ID, 'input-confirm')
    privacy_policy_click=(By.XPATH, '//*[@id="content"]/form/div/div/input[1]')
    continue_button = (By.XPATH, '//*[@id="content"]/form/div/div/input[2]')
    radio_button_yes=(By.XPATH, '//*[@id="content"]/form/fieldset[3]/div/div/label[1]')
    firstname_assert = (By.XPATH,'//*[@id="account"]/div[2]/div/div')
    lastname_assert = (By.XPATH,'//*[@id="account"]/div[3]/div/div')
    emailassert = (By.XPATH,'//*[@id="account"]/div[4]/div/div')
    validemail = (By.XPATH,'//*[@id="account"]/div[4]/div/div')
    register_success = (By.XPATH,'//*[@id="content"]/h1')
    email_exist= (By.XPATH,'//*[@id="account-register"]/div[1]')





    def my_account_click(self):
        self.driver.find_element(*Registration.my_account).click()

    def register_click(self):
        self.driver.find_element(*Registration.register_button).click()

    def first_name(self):
        self.driver.find_element(*Registration.firstname).send_keys("ujjwal")

    def last_name(self):
        self.driver.find_element(*Registration.lastname).send_keys("kumar")

    def email(self):
        self.driver.find_element(*Registration.emails).send_keys(new_email)

    def email_1(self):
        self.driver.find_element(*Registration.emails).send_keys(new_email1)

    def phone_number(self):
        self.driver.find_element(*Registration.mobilenumber).send_keys("1234567890")

    def new_password(self):
        self.driver.find_element(*Registration.newpassword).send_keys("Abcdef@123456")

    def confirm_password(self):
        self.driver.find_element(*Registration.confirmpassword).send_keys("Abcdef@123456")

    def privacy_policy(self):
        self.driver.find_element(*Registration.privacy_policy_click).click()

    def continues(self):
        self.driver.find_element(*Registration.continue_button).click()

    def radio_button(self):
        self.driver.find_element(*Registration.radio_button_yes).click()

    def fields_assert(self):
        assert self.driver.find_element(*Registration.firstname_assert).text =='First Name must be between 1 and 32 characters!'
        assert self.driver.find_element(*Registration.lastname_assert).text == 'Last Name must be between 1 and 32 characters!'

    def email_assert(self):
        assert self.driver.find_element(*Registration.emailassert).text == 'E-Mail Address does not appear to be valid!'

    def valid_email(self):
        self.driver.find_element(*Registration.validemail)

    def assert_registration(self):
        assert self.driver.find_element(*Registration.register_success).text == "Your Account Has Been Created!"

    def first_name_blank(self):
        self.driver.find_element(*Registration.firstname).send_keys("")

    def last_name_blank(self):
        self.driver.find_element(*Registration.lastname).send_keys("")

    def email_blank(self):
        self.driver.find_element(*Registration.emails).send_keys('')

    def phone_number_blank(self):
        self.driver.find_element(*Registration.mobilenumber).send_keys("")

    def new_password_blank(self):
        self.driver.find_element(*Registration.newpassword).send_keys("")

    def confirm_password_blank(self):
        self.driver.find_element(*Registration.confirmpassword).send_keys("")

    def email_duplicate(self):
        assert self.driver.find_element(*Registration.email_exist).text == 'Warning: E-Mail Address is already registered!'






