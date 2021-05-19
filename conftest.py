import pytest
import os

from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", choices=["chrome", "firefox", "opera", "ie"])
    parser.addoption("--url", action="store", default="http://localhost")
    parser.addoption("--drivers", action="store", default=os.path.expanduser("D:\drivers"))
    parser.addoption("--headless", action="store_true", help="Run headless")


@pytest.fixture
def browser(request):
    browser = request.config.getoption("--browser")
    url = request.config.getoption("--url")
    drivers = request.config.getoption("--drivers")
    headless = request.config.getoption("--headless")

    if browser == "chrome":
        chrome_options = webdriver.ChromeOptions()
        chrome_options.headless = headless
        driver = webdriver.Chrome(executable_path=drivers + "/chromedriver", options=chrome_options)
    elif browser == "firefox":
        firefox_options = webdriver.FirefoxOptions()
        firefox_options.headless = headless
        driver = webdriver.Firefox(executable_path=drivers + "/geckodriver", options=firefox_options)
    elif browser == "opera":
        driver = webdriver.Opera(executable_path=drivers + "/operadriver")
    elif browser == "ie":
        if headless:
            driver = webdriver.Ie(executable_path=drivers + "/headless_ie_selenium")
        else:
            driver = webdriver.Ie(executable_path=drivers + "/IEDriverServer")
    else:
        driver = webdriver.Safari()

    driver.maximize_window()

    request.addfinalizer(driver.close)

    driver.get(url)
    driver.url = url

    return driver
