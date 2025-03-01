from selenium.webdriver.common.by import By


class Registration:

    def __init__(self,driver):
        self.driver = driver


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
    emailassert = (By.XPATH,"//div[@class='alert alert-danger alert-dismissible']")
    validemail = (By.XPATH,'//*[@id="account"]/div[4]/div/div')
    register_success = (By.XPATH,'//*[@id="content"]/h1')




    def my_account_click(self):
        return self.driver.find_element(*Registration.my_account)

    def register_click(self):
        return self.driver.find_element(*Registration.register_button)

    def first_name(self):
        return self.driver.find_element(*Registration.firstname)

    def last_name(self):
        return self.driver.find_element(*Registration.lastname)

    def email(self):
        return self.driver.find_element(*Registration.emails)

    def phone_number(self):
        return self.driver.find_element(*Registration.mobilenumber)

    def new_password(self):
        return self.driver.find_element(*Registration.newpassword)

    def confirm_password(self):
        return self.driver.find_element(*Registration.confirmpassword)

    def privacy_policy(self):
        return self.driver.find_element(*Registration.privacy_policy_click)

    def continues(self):
        return self.driver.find_element(*Registration.continue_button)

    def radio_button(self):
        return self.driver.find_element(*Registration.radio_button_yes)

    def first_name_assert(self):
        return self.driver.find_element(*Registration.firstname_assert)

    def last_name_assert(self):
        return self.driver.find_element(*Registration.lastname_assert)

    def email_assert(self):
        return self.driver.find_element(*Registration.emailassert)

    def valid_email(self):
        return self.driver.find_element(*Registration.validemail)

    def registration(self):
        return self.driver.find_element(*Registration.register_success)


