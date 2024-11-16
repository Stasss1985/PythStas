from selenium import webdriver
from selenium.webdriver.common.by import By
import time


try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    inputFirst_name = browser.find_element(
        By.CSS_SELECTOR, '[placeholder="Enter first name"]')
    inputFirst_name.send_keys("Stanislav")
    inputLast_name = browser.find_element(
        By.CSS_SELECTOR, '[placeholder="Enter last name"]')
    inputLast_name.send_keys("Krivko")
    inputEmail = browser.find_element(
        By.CSS_SELECTOR, '[placeholder="Enter email"]')
    inputEmail.send_keys("Stass_66@mail.ru")

# Элемент в форме, который выглядит, как кнопка добавления файла,
# имеет атрибут type="file". Мы должны сначала найти этот элемент
#  с помощью селектора, а затем применить к нему метод send_keys.

    choose_file_btn = browser.find_element(By.CSS_SELECTOR, '[name="file"]')
# это я пробывал кликать - browser.execute_script("arguments[0].click();", choose_file_btn)
    choose_file_btn.send_keys("C:/PythStas/file.txt")

    button = browser.find_element(By.CLASS_NAME, "btn.btn-primary")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
