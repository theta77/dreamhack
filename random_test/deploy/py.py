from selenium import webdriver
import time

driver = webdriver.Chrome("chromedriver.exe")

driver.get("http://host3.dreamhack.games:8738/")
time.sleep(2)