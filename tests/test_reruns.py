from time import sleep

source = "http://selenium1py.pythonanywhere.com/"


def test_guest_should_see_login_link_pass(browser):
    sleep(1)
    browser.get(source)
    print(source)
    browser.find_element_by_css_selector("#login_link")


def test_guest_should_see_login_link_fail(browser):
    sleep(1)
    browser.get(source)
    print(source)
    browser.find_element_by_css_selector("#magic_link")
