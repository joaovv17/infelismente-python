from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys 
import time
navegador = webdriver.Edge()

navegador.get("https://www.youtube.com/")
time.sleep(3)

campo = navegador.find_element(By.NAME, "search_query")
campo.send_keys("chef otto")
campo.send_keys(Keys.ENTER)

time.sleep(6)

primeiroVideo = navegador.find_element(By.ID, "video-title")
primeiroVideo.click()

time.sleep(7)