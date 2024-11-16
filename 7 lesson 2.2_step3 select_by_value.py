from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select


try:
    link = "https://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    number1 = browser.find_element(By.ID, 'num1').text
    number2 = browser.find_element(By.ID, 'num2').text
    sum_numbers = int(number1)+int(number2)
    print(sum_numbers)

    input_fild = Select(browser.find_element(By.TAG_NAME, "select"))
    input_fild.select_by_value(str(sum_numbers))
    time.sleep(3)

    # Отправка формы (если необходимо)
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()


finally:
    time.sleep(8)
    browser.quit()
