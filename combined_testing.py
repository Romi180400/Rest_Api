import requests

import pymysql

from selenium import webdriver

from selenium.webdriver.chrome.service import Service

from selenium.webdriver.common.by import By

import json

user_id = int(input("Please Enter user_id: "))
user_name = input("Please input a user_name")

try:

    res = requests.post(f'http://127.0.0.1:5000/api/users/userData/{user_id}', json={"user_name": f"{user_name}"})
    if res.status_code==201:
        print("User is been added succesfully")
    elif res.status_code==500:
        raise Exception("User already exists")
except Exception as x:
    print(x)
     
try:

    res = requests.get(f'http://127.0.0.1:5000/api/users/userData/{user_id}')
    if res.ok:
        print(res.json())
    elif res.status_code==404:
        raise Exception("Empty user line")
except Exception as y:
    print(y)   
    
try:
    
    conn = pymysql.connect(host='sql.freedb.tech', port=3306, user='freedb_freedb_test123456', passwd='UWk2nu8b8#2%82G', db='freedb_sql.freedb.tech2')
    cursor = conn.cursor()

    cursor.execute(f"SELECT * FROM users WHERE id = {user_id}")
    
    value=cursor.fetchone()
    cursor.close()
    conn.close()
    print(f"The user with the id {user_id} is : " + value[1])
except Exception as z:
    print(z)
    
    
try:
    
    driver = webdriver.Chrome(service=Service("C:\\programming\\selenium\\chromedriver"))
    driver.implicitly_wait(10)
    driver.get(f"http://127.0.0.1:5000/api/users/userData/{user_id}")
    print("API responding")
    name = driver.find_element(By.TAG_NAME, value=("pre"))
    data = json.loads(name.text)
    if data[1] == user_name:
        print("Selenium test succesfull")
    else:
        raise Exception("Test failed")
    driver.quit()
except Exception as r:
    print()