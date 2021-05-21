from pages.main_page import MainPage
import time

# зайти на yandex.ru +
# проверить наличие поля поиска +
# ввести в поиск tensor.ru +
# проверить что появилась панель с подсказками +
# при нажатии enter появляются результаты поиска
# в первых 5 результатах есть ссылка на tensor.ru


def test_search_pan_has_suggestions_to_text(browser):
    link = "https://yandex.ru/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_search_pan()
    page.send_tensor_to_search_pan()
    assert not page.should_be_suggestions_to_text()


def test_if_there_are_search_results(browser):
    link = "https://yandex.ru/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_search_pan()
    page.search_tensor()
    assert not page.should_be_search_results()


def test_if_tensor_is_in_top5_results(browser):
    link = "https://yandex.ru/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_search_pan()
    page.search_tensor()
    assert not page.check_first_five_results()
