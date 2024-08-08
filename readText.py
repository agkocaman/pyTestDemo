from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

service = Service("./drivers/chromedriver")
driver = webdriver.Chrome(service=service)

driver.get("https://tr.wikipedia.org/wiki/Anasayfa")
haftaninSeckinMaddesi = driver.find_element(By.ID, "mp-tfa")
split = haftaninSeckinMaddesi.text.split(",")
print(split[0])

gununKaliteliMaddesi = driver.find_element(By.ID, "mf-tfp").text.split(",")
print(gununKaliteliMaddesi[0])