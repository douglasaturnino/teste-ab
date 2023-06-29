from selenium import webdriver
import numpy as np
import time

driver = webdriver.Chrome()

driver.get('http://127.0.0.1:5000/home')

clicks = 10000

for click in range(clicks):
    if np.random.random() <= 0.3:
        time.sleep(1)
        driver.find_element('name', 'yescheckbox').click()
        driver.find_element('id', 'yesbtn').click()

    else:
        time.sleep(1)
        driver.find_element('name', 'nocheckbox').click()
        driver.find_element('id', 'nobtn').click()

    