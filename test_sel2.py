from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://ru.wikipedia.org/wiki/%D0%9A%D0%BE%D1%88%D0%BA%D0%B0")
try:
  elem = driver.find_element(By.ID, "firstHeading")
  print('элемент найден')
except:
  print ('элемент не найден')
