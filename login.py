from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

service = Service("./drivers/chromedriver")
driver = webdriver.Chrome(service=service)


def test_login(username, password):
    driver.get("https://the-internet.herokuapp.com/login")
    user = driver.find_element(By.ID, "username")
    user.send_keys(username)
    passw = driver.find_element(By.ID, "password")
    passw.send_keys(password)
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    alert = driver.find_element(By.ID, "flash").text
    return alert

#yanlış bigiler ile
message = test_login("x","x")
if "invalid" in message:
    print("hatalı mesaj doğru")

#doğru bilgiler ile
message = test_login("tomsmith","SuperSecretPassword!")
if "secure" in message:
    print("giriş başarılı")
    
#Logout
logOutButton = driver.find_element(By.CSS_SELECTOR, "a.button").click()

h2 = driver.find_element(By.TAG_NAME, "h2")
if "Login Page" in h2.text:
    print("Logout is successful")



