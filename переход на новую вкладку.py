from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/redirect_accept.html")

try:
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    new_window = browser.window_handles
    browser.switch_to.window(new_window[1])

    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)

    # вводим ответ
    input_field = browser.find_element(By.ID, "answer")
    input_field.send_keys(y)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    time.sleep(10)

finally:
    browser.quit()
