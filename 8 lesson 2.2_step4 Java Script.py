from selenium import webdriver
import time

try:
    link = "https://pikabu.ru/best"
    browser = webdriver.Chrome()
    browser.get(link)
    browser.execute_script("alert('Robots at work Ежики пиронженки');")

#    Можно с помощью этого метода выполнить сразу несколько инструкций,
#  перечислив их через точку с запятой.
# Изменим сначала заголовок страницы, а затем вызовем alert:
finally:
    time.sleep(5)
    browser.quit()
