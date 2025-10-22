from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys 
import time
navegador = webdriver.Edge()

navegador.get("https://books.toscrape.com")
time.sleep(3)

campo = navegador.find_element(By.CLASS_NAME, "image_container")
campo.click()

time.sleep(6)