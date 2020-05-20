from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/selects1.html")

    x_element = browser.find_element_by_css_selector("#num1")  # находим веб-элемент x
    x = x_element.text  # отделяем х

    y_element = browser.find_element_by_css_selector("#num2")  # находим веб-элемент y
    y = y_element.text  # отделяем y

    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_visible_text(str(int(x)+int(y))).click()  # ищем элемент с текстом "Python"

    button = browser.find_element_by_tag_name(".btn btn-default").click()

finally:
    # успеваем скопировать код за 10 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

    # не забываем оставить пустую строку в конце файла