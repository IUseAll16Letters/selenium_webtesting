import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption(
                    '--language', action='store',
                    choices=('es', 'fr', 'ru', 'en'),
                    default='ru',
                    help='Select required language: ru, es, en, fr'
                    )
    parser.addoption(
                     '--browser', action='store',
                     choices=('chrome', 'firefox'),
                     default='chrome',
                     help='Optional test for browsers: chrome or firefox'
                    )


@pytest.fixture(scope='function')
def user_language(request):
    return request.config.getoption('language')


@pytest.fixture(scope='function')
def browser(request, user_language):
    browser_name = request.config.getoption('browser')
    if browser_name.lower() in 'chrome':
        print(f"\n>> starting browser chrome, on language: {user_language}")
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        browser = webdriver.Chrome(options=options)
    elif browser_name.lower() in 'firefox':
        print(f"\n>> starting browser firefox, on language: {user_language}")
        options = webdriver.FirefoxOptions()
        options.set_preference("intl.accept_languages", user_language)
        browser = webdriver.Firefox(options=options)
    else:
        raise pytest.UsageError(f'--browser got wrong attr, expected chrome or firefox, got {browser_name} instead')

    browser.maximize_window()
    yield browser
    print('\n>> tearing down browser after test')
    browser.quit()
