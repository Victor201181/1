import math
import time
from selenium import webdriver

# прописываем функцию для подсчета значения х
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome() # открываем браузер
    browser.get(link) # открываем целевую страницу

    x_element = browser.find_element_by_css_selector("#input_value") # находим веб-элемент x
    x = x_element.text # отделяем х
    y = calc(x) #считаем по функции

    input1 = browser.find_element_by_css_selector("#answer") #находим поле кудо надо ввести
    input1.send_keys(y) # вводим полученное значение

    option1 = browser.find_element_by_css_selector("#robotCheckbox") #находим галочку
    option1.click() #нажимаем

    option2 = browser.find_element_by_css_selector("#robotsRule")
    option2.click()

    button = browser.find_element_by_css_selector("[type='submit']")
    button.click()

finally:
    # успеваем скопировать код за 10 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

    # не забываем оставить пустую строку в конце файла




