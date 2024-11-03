import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()
browser.get('https://erp-test.karman24.ru/')
time.sleep(3)

imputMail = browser.find_element(By.XPATH, '//*[@id="email"]')
imputMail.send_keys('krivko.su@codeagency.ru')

imputPassword = browser.find_element(By.XPATH, '//*[@id="password"]')
imputPassword.send_keys('DLNKsfd3214$%23')


try:
    # Ожидание до 5 секунд, пока элемент станет доступен
    imputButton = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.CLASS_NAME, 'btn.btn-primary'))
    )
    imputButton.click()  # Вызов метода click()
except Exception as e:
    print(f"Ошибка: {e}")
finally:
    time.sleep(3)  # Ждем 3 секунд, чтобы увидеть результат

try:
    # Ожидание до 5 секунд, пока кнопка "Сменить" станет доступной.
    changeButton = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable(
            (By.CLASS_NAME, 'p-button.p-component.mt-2.p-button-warning'))
    )
    changeButton.click()  # Вызов метода click()
    time.sleep(5)
    # Ожидание до 5 сек, пока Кнопка офис "ООО 1 мая" станет доступной.
    imput_Office = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable(
            (By.TAG_NAME, 'input')))
    imput_Office.send_keys('Краснодар-1-го Мая ЛОМБАРД (Карман)')

    imput_Office.click()  # Вызов метода click()

except Exception as e:
    print(f"Ошибка: {e}")
finally:
    time.sleep(5)  # Ждем 3 секунд, чтобы увидеть результат


try:
    lead_href = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="leftside-menu-container"]/div[1]/div[2]/div/div/div/ul/li[2]/a'))
    )
    lead_href.click()
except Exception as e:
    print(f"Ошибка {e}")
finally:
    time.sleep(5)

# lead_href = browser.find_element(
#    By.XPATH, '//*[@id="leftside-menu-container"]/div[1]/div[2]/div/div/div/ul/li[2]/a')
# lead_href.click()
# time.sleep(10)

browser.quit()  # Закрываем браузер
