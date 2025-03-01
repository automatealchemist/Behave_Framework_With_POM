from selenium.webdriver.common.by import By


class Search:
    def __init__(self,driver):
        self.driver = driver

    search_k = (By.NAME, 'search')
    searchbutton = (By.XPATH, '//*[@id="search"]/span/button')
    searchresult = (By.LINK_TEXT,"HP LP3065")
    searchtext = (By.XPATH, '//*[@id="content"]/p[2]')

    def search_keyword(self):
        return self.driver.find_element(*Search.search_k)

    def search_button(self):
        return self.driver.find_element(*Search.searchbutton)

    def search_result(self):
        return self.driver.find_element(*Search.searchresult)

    def search_text(self):
        return self.driver.find_element(*Search.searchtext)


