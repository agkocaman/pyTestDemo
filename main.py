from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service = Service("./drivers/chromedriver")
driver = webdriver.Chrome(service=service)

driver.get("https://www.python.org")

link = driver.current_url
title = driver.title
if "python.org" in link:
    print("Bu sayfa Python.org sitesine aittir.1")
if "Python.org" in title:
    print("Bu sayfa Python.org sitesine aittir.2")
driver.get("https://www.google.com")
link = driver.current_url
title = driver.title
print(title+"deneme")
if "google" in link:
    print("Bu sayfa google sitesine aittir.3")
if "Google" in title:
    print("Bu sayfa google sitesine aittir.4")
    
