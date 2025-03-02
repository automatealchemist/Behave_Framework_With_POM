from selenium.webdriver.common.by import By


class Search:
    def __init__(self,driver):
        self.driver = driver

    search_k = (By.NAME, 'search')
    searchbutton = (By.XPATH, '//*[@id="search"]/span/button')
    searchresult = (By.LINK_TEXT,"HP LP3065")
    searchtext = (By.XPATH, '//*[@id="content"]/p[2]')

    def search_valid_keyword(self):
        self.driver.find_element(*Search.search_k).send_keys("HP")

    def search_button(self):
        self.driver.find_element(*Search.searchbutton).click()

    def search_result(self):
        assert self.driver.find_element(*Search.searchresult).is_displayed()
        self.driver.find_element(*Search.searchresult).click()

    def search_text(self):
        sample_text = "There is no product that matches the search criteria."
        assert self.driver.find_element(*Search.searchtext).text.__eq__(sample_text)

    def search_invalid_keyword(self):
        self.driver.find_element(*Search.search_k).send_keys("abcxyz")


