# import pytest

from pages.pictures_page import PicturesPage


# 1) Зайти на yandex.ru
# 2) Ссылка «Картинки» присутствует на странице
# 3) Кликаем на ссылку
# 4) Проверить, что перешли на url https://yandex.ru/images/

# @pytest.mark.skip
def test_yandex_pictures_link(browser):
    link = "https://yandex.ru/"
    page = PicturesPage(browser, link)
    page.open()
    assert not page.should_be_pictures_link(), "Yandex Pictures link is not presented"


# @pytest.mark.skip
def test_click_check_url(browser):
    link = "https://yandex.ru/"
    page = PicturesPage(browser, link)
    page.open()
    page.go_to_pictures()
    page.switch_tabs_up()
    assert not page.check_actual_url()

# 5) Открыть 1 категорию, проверить что открылась, в поиске верный текст
# 6) Открыть 1 картинку , проверить что открылась
# 7) При нажатии кнопки вперед картинка изменяется
# 8) При нажатии кнопки назад картинка изменяется на изображение из шага 6. Необходимо
# проверить, что это то же изображение.


# @pytest.mark.skip
def test_category(browser):
    link = "https://yandex.ru/images/"
    page = PicturesPage(browser, link)
    page.open()
    page.go_to_first_category()
    assert not page.go_to_first_picture_in_cat()


def test_next_prev_pic(browser):
    link = "https://yandex.ru/images/"
    page = PicturesPage(browser, link)
    page.open()
    page.go_to_first_category()
    page.go_to_first_picture_in_cat()
    assert not page.next_prev_pic()

