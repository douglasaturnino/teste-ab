from selenium import webdriver
import numpy as np
import time

options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')

driver = webdriver.Chrome(options=options)

driver.get('http://mab-web-1:5000/home')

clicks = 1000

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