from selenium import webdriver
import numpy as np


path_webdriver = '/mnt/0165652C522E8ECA/ProjetosDeProgramacao/AB-testing/PA-james/pa_bayesion/geckodriver'
driver = webdriver.Chrome()


driver.get('http://127.0.0.1:5000/home')

clicks = 10000

for click in range(clicks):
    if np.random.random() < 0.5:
        driver.find_element('name', 'yescheckbox').click()
        driver.find_element('id', 'yesbtn').click()

    else: 
        driver.find_element('name', 'nocheckbox').click()
        driver.find_element('id', 'nobtn').click()
