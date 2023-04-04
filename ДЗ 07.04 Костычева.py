from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
driver.get("https://makarova1507ana.github.io/registration_page/")

elements = driver.find_elements(By.TAG_NAME, "input") #ищем элемент
# # find_elements формирует список
print(len(elements))# узнаем длину списка
for i in range(3):# range 0, 1, 2
    if i == 3:
        continue
    elements[i].send_keys("b")
    time.sleep(5)

     #  дописать юнит тест, не успела


