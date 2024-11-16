# В этой задаче вам нужно написать программу,
#  которая будет выполнять следующий сценарий:

# Открыть страницу http://suninjuly.github.io/explicit_wait2.html
# Дождаться, когда цена дома уменьшится до $100
#  (ожидание нужно установить не меньше 12 секунд)
# Нажать на кнопку "Book"
# Решить уже известную нам математическую задачу
# (используйте ранее написанный код) и отправить решение
# Чтобы определить момент, когда цена аренды уменьшится до $100,
#  используйте метод text_to_be_present_in_element из
# библиотеки expected_conditions.


from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import time


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/explicit_wait2.html")

button = WebDriverWait(browser, 15).until(
    EC.element_to_be_clickable((By.ID, 'book')))
# говорим Selenium проверять в течение 5 секунд, пока текст цена не станет = 100$
price_find = WebDriverWait(browser, 15).until(
    EC.text_to_be_present_in_element((By.ID, "price"), "$100")
)
button.click()

scroll_find_btn = browser.find_element(By.ID, 'solve')
browser.execute_script(
    "return arguments[0].scrollIntoView(true);", scroll_find_btn)

x_element = browser.find_element(By.CSS_SELECTOR, '[id="input_value"]')
x = x_element.text

imput_answer = browser.find_element(By.ID, 'answer')
imput_answer.send_keys(calc(x))

scroll_find_btn.click()

time.sleep(8)
# закрываем браузер после всех манипуляций
browser.quit()
