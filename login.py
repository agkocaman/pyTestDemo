from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

service = Service("./drivers/chromedriver")
driver = webdriver.Chrome(service=service)


# Yanlış bilgilerle
driver.get("https://the-internet.herokuapp.com/login")
username = driver.find_element(By.ID, "username")
username.send_keys("tomsmith1")

password = driver.find_element(By.ID, "password")
password.send_keys("SuperSecretPassword!1")
loginButton = driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

alert = driver.find_element(By.ID, "flash")
if "Your username is invalid" in alert.text:
    print("Error Login is successful")


# Doğru bilgiler ile
driver.get("https://the-internet.herokuapp.com/login")
username = driver.find_element(By.ID, "username")
username.send_keys("tomsmith")

password = driver.find_element(By.ID, "password")
password.send_keys("SuperSecretPassword!")
loginButton = driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

h2 = driver.find_element(By.TAG_NAME, "h2")
if "Secure" in h2.text:
    print("Login is successful")



#Logout
logOutButton = driver.find_element(By.CSS_SELECTOR, "a.button").click()

h2 = driver.find_element(By.TAG_NAME, "h2")
if "Login Page" in h2.text:
    print("Logout is successful")