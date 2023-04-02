from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://makarova1507ana.github.io/registration_page/")
elements = driver.find_elements(By.TAG_NAME, "input")
print(len(elements)) #len считает длину списка
for i in list(range(3)): #list список с конца
    elements[i-3].send_keys("b")
time.sleep(5)
driver.save_screenshot('screen.png')
