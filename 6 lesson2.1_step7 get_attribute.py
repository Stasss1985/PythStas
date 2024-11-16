from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


link = "http://suninjuly.github.io/get_attribute.html"
browser = webdriver.Chrome()
browser.get(link)
time.sleep(5)


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


images_chest = browser.find_element(By.ID, "treasure")
x_get_valuex_images_chest = images_chest.get_attribute("valuex")
x = x_get_valuex_images_chest


imput_answer = browser.find_element(By.ID, 'answer')
imput_answer.send_keys(calc(x))

imput_robotCheckbox = browser.find_element(By.ID, 'robotCheckbox').click()

imput_robotsRule = browser.find_element(By.ID, 'robotsRule').click()

submit_btn = browser.find_element(By.CLASS_NAME, 'btn').click()
# ожидание чтобы визуально оценить результаты прохождения скрипта
time.sleep(10)
# закрываем браузер после всех манипуляций
browser.quit()
