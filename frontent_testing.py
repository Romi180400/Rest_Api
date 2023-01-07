from selenium import webdriver

from selenium.webdriver.chrome.service import Service

from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=Service("C:\\programming\\selenium\\chromedriver"))
driver.implicitly_wait(10)
driver.get("http://127.0.0.1:5001/api/users/getUser/5")
print("site responding")
name = driver.find_element(By.ID, value="5").text
print("The name is:", name)
driver.quit()
