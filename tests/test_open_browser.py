import time


def test_open_browsers(browser):
    browser.get(browser.url)
    # Проверка того, что это Opencart
    browser.find_element_by_xpath("//*[text()='OpenCart']")
    # Проверка того, что это главная страница
    browser.find_element_by_class_name("swiper-viewport")
    time.sleep(2)  # Для демонстрации
