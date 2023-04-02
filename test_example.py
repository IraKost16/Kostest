from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time



driver = webdriver.Chrome() # подключаю драйвер
driver.get("https://makarova1507ana.github.io/registration_page/") # делаем запрос на открытие страницы
#
# l = [1, 5, 3] # пример списка
# #print(l[0])
#
# #первый способ без индексов
# for element in l:
#     print(element)
#
# #второй способ с индексами
# for index in range(len(l)):
#     print("index = ", index, "l[index]", l[index])


elements = driver.find_elements(By.TAG_NAME, "input") #ищем элемент
# # find_elements формирует список
print(len(elements))# узнаем длину списка
for i in range(5):# range 0, 1, 2
    if i == 3:
        continue
    elements[i].send_keys("b")
    if i == 4:
        elements[i].click()#нажать на сам элемент
phone = driver.find_element(By.XPATH, '/html/body/main/form/input[6]')
time.sleep(5)


# import datetime
# id = datetime.datetime.now()
# id = str(id).replace(' ', '') #id[:id.find(' ')]+id[:id.find(' ')+1:]
# print(id)
# name = 'screen' + str(id)+'.png'
# print(name)
# driver.get_screenshot_as_png()





#############################################################
# elements = driver.find_elements(By.TAG_NAME, "input") #ищем элемент
# # find_elements формирует список
# # print(elements[0])
# time.sleep(5)
# elements[2].send_keys("почта")# отправить значение в форму
# time.sleep(5)
# # elem.send_keys(Keys.RETURN)# нажатие клавиши enter
# time.sleep(2)



