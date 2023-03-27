import time
import pytest

from selenium.webdriver.common.by import By


link = 'http://selenium1py.pythonanywhere.com/catalogue/hacking-exposed-wireless_208/'

def test_presence_cart_button(browser):
    browser.implicitly_wait(5)
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, '.btn-add-to-basket')
    time.sleep(10)

    button_name = browser.find_element(By.CSS_SELECTOR, '.btn-add-to-basket').text

    assert 
    

if __name__ == "__main__":
    pytest.main()