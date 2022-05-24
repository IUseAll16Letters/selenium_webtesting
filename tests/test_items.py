from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

source = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

language_configuration = {'es': 'Añadir al carrito',
                          'fr': 'Ajouter au panier',
                          'ru': 'Добавить в корзину',
                          'en': 'Add to basket'}


def test_locale_languages(browser, request):
    browser.get(source)

    language_received = request.config.getoption('language')
    required_response = language_configuration.get(language_received)

    WebDriverWait(browser, 5).until(ec.element_to_be_clickable((By.CSS_SELECTOR, 'button[value]')))
    res = browser.find_element(by=By.CSS_SELECTOR, value='button[value]').get_attribute('value')
    print(f'\nselected language = {language_received}')
    sleep(5)

    assert required_response == res, f'Expected get {required_response}, got {res} instead'
