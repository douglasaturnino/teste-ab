from selenium import webdriver
import numpy as np
import time

driver = webdriver.Chrome()

driver.get('http://127.0.0.1:5000/home')

clicks = 10000

for click in range(clicks):
    button_color = driver.find_element('name', 'forwardbtn').get_attribute('value')

    if button_color == 'blue':

        if np.random.random() <= 0.30:
            driver.find_element('name', 'yescheckbox').click()
            driver.find_element('id', 'yesbtn').click()

        else:
            driver.find_element('name', 'nocheckbox').click()
            driver.find_element('id', 'nobtn').click()
    else:
        if np.random.random() <= 0.32:
            driver.find_element('name', 'yescheckbox').click()
            driver.find_element('id', 'yesbtn').click()
        else:
            driver.find_element('name', 'nocheckbox').click()
            driver.find_element('id', 'nobtn').click()
    
    time.sleep(0.2)   