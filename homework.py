from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
import math
import os
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait



link = "http://suninjuly.github.io/explicit_wait2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "100"))   
    btn = browser.find_element(By.CSS_SELECTOR, "[id=book]")
    btn.click()
    x = WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.ID, "input_value")))
    x_value = x.text
    y = str(math.log(abs(12 * math.sin(int(x_value)))))
    answer = browser.find_element(By.ID, "answer")
    answer.send_keys(y)
    submit = browser.find_element(By.CSS_SELECTOR, "[type=submit]")
    submit.click()
     

finally:
    time.sleep(30)
    browser.quit()


