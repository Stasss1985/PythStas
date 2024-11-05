import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


browser = webdriver.Chrome()
browser.get('https://erp-test.karman24.ru/')
browser.maximize_window()
WebDriverWait(browser, 10).until(
    EC.element_to_be_clickable((By.CLASS_NAME, 'btn.btn-primary'))
)
imputMail = browser.find_element(By.ID, 'email')
imputMail.send_keys('krivko.su@codeagency.ru')

imputPassword = browser.find_element(By.ID, 'password')
imputPassword.send_keys('DLNKsfd3214$%23')

imputButton = browser.find_element(By.CLASS_NAME, 'btn.btn-primary')
imputButton.click()
# Ожидание до 5 секунд, пока кнопка "Сменить" станет доступной.
WebDriverWait(browser, 10).until(
    EC.text_to_be_present_in_element((By.TAG_NAME, 'body'), 'Сменить'))

changeButton = browser.find_element(
    By.CLASS_NAME, 'p-button.p-component.mt-2.p-button-warning')
changeButton.click()

input_fild = browser.find_element(By.CLASS_NAME, 'p-tree-filter-container')
input_fild.click()

input_fild2 = WebDriverWait(browser, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, '[aria-label="Краснодар-1-го Мая ЛОМБАРД (Карман)"]')))
input_fild2.click()
# input_fild2 = browser.find_element(
#    By.CSS_SELECTOR, '[aria-label="Краснодар-1-го Мая ЛОМБАРД (Карман)"]')

# input_fild2 = browser.find_element(
#    By.XPATH, '/html/body/div[2]/div/div[2]/div/div[2]/ul/li[10]/ul/li[10]/div/span[2]')
# time.sleep(5)
# time.sleep(10)
# WebDriverWait(browser, 10).until(
#    EC.text_to_be_present_in_element((By.TAG_NAME, 'body'), 'Лиды'))
# lead_href = browser.find_element(By.CSS_SELECTOR, '[href="/lead"]')
# lead_href.click()
# href = "/lead/create"


# lead_href = browser.find_element(
#    By.XPATH, '//*[@id="leftside-menu-container"]/div[1]/div[2]/div/div/div/ul/li[2]/a')
# lead_href.click()
# time.sleep(10)

lead_href = WebDriverWait(browser, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, '[href="/lead"]')))
lead_href.click()

lead_create_grin = WebDriverWait(browser, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, '[href = "/lead/create"]')))
lead_create_grin.click()

counteragent_choose = WebDriverWait(browser, 10).until(
    EC.element_to_be_clickable((By.ID, 'counteragentId')))
counteragent_choose.click()

counteragent_choose2 = browser.find_element(
    By.CSS_SELECTOR, '[aria-controls="counteragentId_list"]')
counteragent_choose2.send_keys('Кривко С.Ю.')

counteragent_choose2 = WebDriverWait(browser, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, '[aria-label="Кривко С.Ю."]')))
counteragent_choose2.click()


time.sleep(7)
browser.quit()  # Закрываем браузер
