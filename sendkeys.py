from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

service = Service("./drivers/chromedriver")
driver = webdriver.Chrome(service=service)

driver.get("https://duckduckgo.com/")

aramaKutusu = driver.find_element(By.ID, "searchbox_input")
aramaKutusu.send_keys("selenium")
aramaKutusu.send_keys(Keys.ENTER)

title = driver.title
if "selenium at DuckDuckGo" in title:
    print("Arama sonucunda selenium kelimesi gosterilmistir.")


driver.get("https://google.com/")

aramaKutusu = driver.find_element(By.NAME, "q")
aramaKutusu.send_keys("selenium")
aramaKutusu.send_keys(Keys.ENTER)

title = driver.title
if "selenium - Google'da Ara" in title:
    print("Arama sonucunda selenium kelimesi gosterilmistir.")

