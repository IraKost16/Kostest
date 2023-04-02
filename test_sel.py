from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time

driver = webdriver.Chrome()
driver.get("https://makarova1507ana.github.io/registration_page")
elem = driver.find_element(By.NAME, "fname")
elem.send_keys("Irina")

elem = driver.find_element(By.NAME, "lname")
elem.send_keys("Kostychevaa")

elem = driver.find_element(By.NAME, "birthday")
elem.send_keys("16.01.1983")

elem.send_keys(Keys.RETURN)

driver.close()