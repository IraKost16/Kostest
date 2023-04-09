from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://ru.wikipedia.org/wiki/Кошка")

try:
    element = driver.find_element(By.ID, "firstHeading")
    print("текст соответствует")
except:
    print("текст не соответствует")

head_page = driver.find_element(By.TAG_NAME, 'h1')
text_from_head = head_page.text

searchInput = driver.find_element(By.ID, 'searchInput')
text_from_searchInput = searchInput.get_attribute('placeholder')
searchInput.send_keys(text_from_head)
