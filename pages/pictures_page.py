from .base_page import BasePage
from .locators import MainPageLocators
from .locators import PicturePageLocators


class PicturesPage(BasePage):

    def check_actual_url(self):
        assert self.browser.current_url[:25] == "https://yandex.ru/images/", "Current URL is wrong"

    def should_be_pictures_link(self):
        assert self.is_element_present(*MainPageLocators.PICTURES_LINK), "Pictures link is not presented"

    def go_to_pictures(self):
        self.browser.find_element(*MainPageLocators.PICTURES_LINK).click()

    def go_to_first_category(self):
        cat = self.browser.find_element(*PicturePageLocators.FIRST_CAT_PICTURE)
        # description = cat.get_attribute("data-grid-text")
        self.browser.find_element(*PicturePageLocators.FIRST_CAT_PICTURE).click()
        # decs2 = self.browser.find_element_by_tag_name("title")

    def go_to_first_picture_in_cat(self):
        self.browser.find_element(*PicturePageLocators.FIRST_PICTURE_INSIDE_CAT).click()
        assert self.is_element_present(*PicturePageLocators.OPEN_PICTURE_CONTAINER), "Picture 1 is not open"

    def next_prev_pic(self):
        pic1 = self.browser.find_element(*PicturePageLocators.OPEN_PICTURE_LINK)
        pic1 = pic1.get_attribute("src")

        self.browser.find_element(*PicturePageLocators.NEXT_PICTURE_BUTTON).click()
        self.browser.find_element(*PicturePageLocators.PREV_PICTURE_BUTTON).click()

        pic2 = self.browser.find_element(*PicturePageLocators.OPEN_PICTURE_LINK)
        pic2 = pic2.get_attribute("src")
        assert pic1 == pic2, "1st pic is not the same as before"

