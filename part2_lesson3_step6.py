from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    ...



    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button[type=submit]")
    button.click()


    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    x_element = browser.find_element_by_css_selector('.form-group .nowrap#input_value')
    x = x_element.text
    y = calc(x)
    y_element = browser.find_element_by_css_selector('.form-group #answer  ')
    y_element.send_keys(y)

    button = browser.find_element_by_css_selector("button[type=submit]")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)




finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()