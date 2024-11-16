import time
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get('https://pikabu.ru/best')
time.sleep(5)
button_enter = browser.find_element(
    By.CLASS_NAME, 'pkb-normal-btn header-right-menu__login-button').click()
time.sleep(5)
button_href_ya = browser.find_element(
    By.LINK_TEXT, 'Свежее')
button_href_ya.click()
time.sleep(5)
