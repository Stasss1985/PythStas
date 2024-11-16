from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


link = "https://suninjuly.github.io/math.html"
browser = webdriver.Chrome()
browser.get(link)
time.sleep(5)


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


x_element = browser.find_element(By.CSS_SELECTOR, '[id="input_value"]')
x = x_element.text


imput_answer = browser.find_element(By.ID, 'answer')
imput_answer.send_keys(calc(x))

people_radio = browser.find_element(By.ID, "peopleRule")
# Найдём атрибут "checked" с помощью встроенного метода get_attribute и проверим его значение:
people_checked = people_radio.get_attribute("checked")
print("value of people radio: ", people_checked)
assert people_checked is not None, "People radio is not selected by default"

imput_robotCheckbox = browser.find_element(By.ID, 'robotCheckbox').click()

imput_robotsRule = browser.find_element(By.ID, 'robotsRule').click()

submit_btn = browser.find_element(By.CLASS_NAME, 'btn').click()
# ожидание чтобы визуально оценить результаты прохождения скрипта
time.sleep(10)
# закрываем браузер после всех манипуляций
browser.quit()
