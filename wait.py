from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from math import *


def calc(x):
    return str(log(abs(12*sin(int(x)))))


if __name__ == '__main__':
    try:
        link = "http://suninjuly.github.io/explicit_wait2.html"
        browser = webdriver.Chrome()
        browser.get(link)
        WebDriverWait(browser, 5).until(
            EC.text_to_be_present_in_element((By.ID, "price"), "100")
        )
        button = browser.find_element(By.ID, "book")
        button.click()
        x = browser.find_element(By.ID, "input_value").text
        y = calc(x)
        print(y)
        input1 = browser.find_element(By.ID, "answer")
        input1.send_keys(y)
        btn = browser.find_element(By.ID, "solve")
        btn.click()
    finally:
        time.sleep(30)
        browser.quit()
