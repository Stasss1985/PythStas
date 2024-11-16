import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options


browser = webdriver.Chrome()
browser.get('https://erp-test.karman24.ru/')
browser.execute_script("document.body.style.fontSize = '80%';")
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

time.sleep(3)  # Ожидание до 5 секунд, пока кнопка "Сменить" станет доступной.
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

lead_href = WebDriverWait(browser, 20).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, '[href="/lead"]')))
lead_href.click()

# until(EC.visibility_of_element_located((By.CSS_SELECTOR, "element_css"))).get_attribute("value")

WebDriverWait(browser, 20).until(EC.visibility_of_element_located(
    (By.CLASS_NAME, 'dropdown.notification-list.d-none.d-lg-block')))

lead_create_grin = WebDriverWait(browser, 20).until(
    EC.element_to_be_clickable((By.CLASS_NAME, 'p-button-icon.pi.pi-plus')))
lead_create_grin.click()

WebDriverWait(browser, 20).until(EC.visibility_of_element_located(
    (By.CLASS_NAME, 'dropdown.notification-list.d-none.d-lg-block')))

counteragent_choose2 = WebDriverWait(browser, 20).until(
    EC.element_to_be_clickable((By.ID, 'counteragentId')))
counteragent_choose2.click()

counteragent_choose2 = browser.find_element(
    By.CSS_SELECTOR, '[aria-controls="counteragentId_list"]')
counteragent_choose2.send_keys('Кривко С.Ю.')

counteragent_choose2 = WebDriverWait(browser, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, '[aria-label="Кривко С.Ю."]')))
counteragent_choose2.click()

counteragent_check_btn = WebDriverWait(browser, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, '[aria-label="Проверить"]')))
counteragent_check_btn.click()

WebDriverWait(browser, 10).until(
    EC.element_to_be_clickable((By.ID, 'isTypeTrue')))

pasport_checkboxs = browser.find_elements(By.CLASS_NAME, 'p-checkbox-box')
checkbox1 = (pasport_checkboxs[0]).click()
checkbox2 = (pasport_checkboxs[1]).click()
checkbox3 = (pasport_checkboxs[2]).click()
checkbox4 = (pasport_checkboxs[3]).click()
checkbox5 = (pasport_checkboxs[4]).click()

pasport_confirm = WebDriverWait(browser, 20).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, '[aria-label="Далее"]')))
pasport_confirm.click()

sourceId_chose = WebDriverWait(browser, 20).until(
    EC.element_to_be_clickable((By.ID, 'sourceId')))
sourceId_chose.click()

sourceId_find = browser.find_elements(By.CLASS_NAME, 'sourceId')
sourceId_chose1 = (sourceId_find[0]).click()


time.sleep(7)
browser.quit()
