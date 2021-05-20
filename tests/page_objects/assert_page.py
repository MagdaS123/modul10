from tests.helpers.support_functions import *

text = '//*[@id="post-8"]/header/h1'

def text_visible(driver_instance):
    elem = wait_for_visibility_of_element_by_xpath(driver_instance, text)
    return elem.is_displayed()