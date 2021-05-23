from tests.helpers.support_functions import *
from selenium.webdriver.common.keys import Keys

field_search = 'woocommerce-product-search-field-0'
text = '//*[@id="product-53"]/div[2]/h1'

def field_search_visible(driver_instance):
    elem = wait_for_visibility_of_element(driver_instance, field_search)
    return elem.is_displayed()


def find_item(driver_instance):
    elem = driver_instance.find_element_by_id(field_search)
    elem.send_keys('polo')
    value = 'polo'
    if value == elem.get_attribute("value"):
        action = ActionChains(driver_instance)
        action.key_down(Keys.ENTER).perform()
    else:
        return False


def item_is_find(driver_instance):
    elem = wait_for_visibility_of_element_by_xpath(driver_instance, text)
    return elem.is_displayed()
 