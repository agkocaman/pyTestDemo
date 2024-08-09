import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

service = Service("./drivers/chromedriver")
driver = webdriver.Chrome(service=service)

driver.get("https://www.imdb.com/")
driver.maximize_window()
driver.find_element(By.ID,"imdbHeader-navDrawerOpen").click()
time.sleep(1)
driver.find_element(By.CSS_SELECTOR, "#nav-link-categories-mov + span > div > div  > ul  > a:nth-of-type(2)").click()
time.sleep(1)
dataFilmName = driver.find_elements(By.CSS_SELECTOR, "li > * .ipc-title__text")
dataFilmDate = driver.find_elements(By.CSS_SELECTOR, "li > * .cli-title-metadata > span:nth-of-type(1)")
for i in dataFilmDate:
    if i.text >= '2023':
        print(i.text +"----" +dataFilmName[dataFilmDate.index(i)].text)


    

