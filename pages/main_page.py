from .base_page import BasePage
from selenium.webdriver.common.keys import Keys
from .locators import MainPageLocators


class MainPage(BasePage):
    def should_be_search_pan(self):
        assert self.is_element_present(*MainPageLocators.SEARCH_PAN), "Search panel is not presented"

    def send_tensor_to_search_pan(self):
        a = self.browser.find_element(*MainPageLocators.SEARCH_PAN)
        a.send_keys('Тензор')

    def search_tensor(self):
        self.send_tensor_to_search_pan()
        self.browser.find_element(*MainPageLocators.SEARCH_PAN).send_keys(Keys.ENTER)

    def should_be_suggestions_to_text(self):
        assert self.is_element_present(*MainPageLocators.VISIBLE_SEARCH_SUGGESTIONS), \
            "Search suggestions is not presented"

    def should_be_search_results(self):
        assert self.browser.find_elements_by_css_selector(".OrganicTitle-LinkText.organic__url-text"), \
            "No search results presented"

    def check_first_five_results(self):
        results = self.browser.find_elements_by_css_selector(".Link.Link_theme_outer")
        links = [res.get_attribute('href') for res in results[:5]]
        assert "https://tensor.ru/" in links, "tensor.ru is not in top 5 search results"

