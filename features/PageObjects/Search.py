from selenium.webdriver.common.by import By

from utilities.Baseclass import Baseclass


class Search(Baseclass):
    def __init__(self,driver):
        super().__init__(driver)

    search_name = (By.NAME, 'search')
    searchbutton_xpath = (By.XPATH, '//*[@id="search"]/span/button')
    searchresult_link_text = (By.LINK_TEXT,"HP LP3065")
    searchtext_xpath = (By.XPATH, '//*[@id="content"]/p[2]')

    def search_valid_keyword(self):
        self.send_data("search_name",'search','HP')

    def search_button(self):
        self.click_on_element('searchbutton_xpath','//*[@id="search"]/span/button')


    def search_result(self):
        #assert self.driver.find_element(By.LINK_TEXT,"HP LP3065")
        self.retrieve_element_text_and_verify('searchresult_link_text',"HP LP3065","HP LP3065")
        self.click_on_element("searchresult_link_text","HP LP3065")

    def search_text(self):

        return self.retrieve_element_text_and_verify("searchtext_xpath",'//*[@id="content"]/p[2]',"There is no product that matches the search criteria.")


    def search_invalid_keyword(self):
        self.send_data('search_name','search','"abcxyz"')


