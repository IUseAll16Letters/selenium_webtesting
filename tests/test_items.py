from time import sleep
from selenium.webdriver.common.by import By

source = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

language_configuration = {'es': 'Añadir al carrito',
                          'fr': 'Ajouter au panier',
                          'ru': 'Добавить в корзину',
                          'en': 'Add to basket'}


def test_should_test(browser, request):
    browser.get(source)
    sleep(3)
    language_received = request.config.getoption('language')
    required_response = language_configuration.get(language_received)
    res = browser.find_element(by=By.CSS_SELECTOR, value='button[value]').get_attribute('value')
    print(f'\nselected language = {language_received}')
    assert required_response == res, f'Expected get {required_response}, got {res} instead'
