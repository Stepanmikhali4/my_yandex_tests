from selenium.webdriver.common.by import By


class MainPageLocators:
    SEARCH_PAN = (By.CSS_SELECTOR, ".input__input")

    PICTURES_LINK = (By.XPATH, '//div[text()="Картинки"]')

    VISIBLE_SEARCH_SUGGESTIONS = (By.CLASS_NAME, "input_ahead-visible_yes")


class PicturePageLocators:
    FIRST_CAT_PICTURE = (By.CSS_SELECTOR, ".PopularRequestList-Item_pos_0")

    PAGE_DESCRIPTION = (By.TAG_NAME, "title")

    FIRST_PICTURE_INSIDE_CAT = (By.CSS_SELECTOR, ".serp-item_pos_0")

    OPEN_PICTURE_CONTAINER = (By.CSS_SELECTOR, ".MMImageContainer")

    OPEN_PICTURE_LINK = (By.CSS_SELECTOR, ".MMImage-Preview")

    NEXT_PICTURE_BUTTON = (By.CSS_SELECTOR, ".CircleButton_type_next")

    PREV_PICTURE_BUTTON = (By.CSS_SELECTOR, ".CircleButton_type_prev")
