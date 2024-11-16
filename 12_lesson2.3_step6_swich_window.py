from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    submit_btn = browser.find_element(By.CSS_SELECTOR, '[type="submit"]')
    submit_btn.click()
# метод window_handles, который возвращает массив имён всех вкладок
    browser.window_handles

# Также мы можем запомнить имя текущей вкладки, чтобы иметь возможность потом к ней вернуться:
# first_window = browser.window_handles[0]
    new_window = browser.window_handles[1]

# Для переключения на новую вкладку надо явно указать, на какую вкладку мы хотим перейти.
# browser.switch_to.window(window_name)
    browser.switch_to.window(new_window)
    time.sleep(3)

    x_element = browser.find_element(By.CSS_SELECTOR, '[id="input_value"]')
    x = x_element.text

    imput_answer = browser.find_element(By.ID, 'answer')
    imput_answer.send_keys(calc(x))

    submit_btn = browser.find_element(By.CLASS_NAME, 'btn').click()

    time.sleep(3)
# Для переключения на первую вкладку надо явно указать, на какую вкладку мы хотим перейти.
# browser.switch_to.window(window_name)
    first_window = browser.window_handles[0]
    browser.switch_to.window(first_window)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
