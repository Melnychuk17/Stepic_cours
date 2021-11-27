from selenium import webdriver
import time
import os

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    ...
    input1 = browser.find_element_by_xpath('//input[@placeholder="Enter first name"]')
    input1.send_keys("Artur")
    input2 = browser.find_element_by_xpath('//input[@placeholder="Enter last name"]')
    input2.send_keys("Palko")
    input3 = browser.find_element_by_xpath('//input[@placeholder="Enter email"]')
    input3.send_keys("super.gudo32@gmail.com")

    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'fiel.txt')  # добавляем к этому пути имя файла
    element=browser.find_element_by_id("file")
    element.send_keys(file_path)


    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button[type=submit]")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()