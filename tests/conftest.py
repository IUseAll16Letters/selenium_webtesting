import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--lang', action='store', default=None,
                     help='Select required language: ru, es, en, fr, zh-CN')


@pytest.fixture(scope='function')
def browser(request):
    language = request.config.getoption("lang")
    browser = None

    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': language})
    print("\nstart chrome browser for test..")
    browser = webdriver.Chrome(options=options)

    yield browser

    print("\nquit browser..")

    browser.quit()
