from tests.helpers.support_functions import *
from selenium.webdriver.support.select import Select
from time import sleep

shop_tab = '//*[@id="menu-item-102"]/a'
dropdown_list = '//*[@id="main"]/div[1]/form/select'


def click_shop_tab(driver_instance):
    wait_for_visibility_of_element_by_xpath(driver_instance, shop_tab)
    elem = driver_instance.find_element_by_xpath(shop_tab)
    elem.click()


def sort_asc(driver_instance):
    elem_list = Select(driver_instance.find_element_by_xpath(dropdown_list))
    wait_for_visibility_of_element_by_xpath(driver_instance, dropdown_list, time_to_wait=1)
    elem_list.select_by_index(4)
    sleep(3)
