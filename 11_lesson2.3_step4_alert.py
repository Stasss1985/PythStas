from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    submit_btn = browser.find_element(By.CSS_SELECTOR, '[type="submit"]')
    submit_btn.click()
    time.sleep(3)
    alert = browser.switch_to.alert
    alert.accept()

    x_element = browser.find_element(By.CSS_SELECTOR, '[id="input_value"]')
    x = x_element.text

    imput_answer = browser.find_element(By.ID, 'answer')
    imput_answer.send_keys(calc(x))

    submit_btn = browser.find_element(By.CLASS_NAME, 'btn').click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
