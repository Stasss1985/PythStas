
from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

browser = webdriver.Chrome()
link = "https://SunInJuly.github.io/execute_script.html"
browser.get(link)


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


find_x = browser.find_element(By.ID, "input_value").text
# x_get_valuex = find_x.get_attribute("span")
x = find_x
print(x)

imput_answer = browser.find_element(By.ID, 'answer')
imput_answer.send_keys(calc(x))

imput_robotCheckbox = browser.find_element(By.ID, 'robotCheckbox').click()

imput_robotsRule = browser.find_element(By.ID, 'robotsRule')
browser.execute_script(
    "return arguments[0].scrollIntoView(true);", imput_robotsRule)
imput_robotsRule.click()

submit_btn = browser.find_element(By.CLASS_NAME, 'btn')
browser.execute_script("return arguments[0].scrollIntoView(true);", submit_btn)
submit_btn.click()
# ожидание чтобы визуально оценить результаты прохождения скрипта
time.sleep(10)
# закрываем браузер после всех манипуляций
browser.quit()
