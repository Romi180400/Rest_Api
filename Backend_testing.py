import requests

import pymysql

user_id = int(input("Please Enter user_id: "))

try:

    res = requests.post(f'http://127.0.0.1:5000//api/users/userData/{user_id}', json={"user_name": "Hadar"})
    if res.status_code==201:
        print("User is been added succesfully")
    elif res.status_code==500:
        raise Exception("User already exists")
except Exception as x:
    print(x)
     
try:

    res = requests.get(f'http://127.0.0.1:5000//api/users/userData/{user_id}')
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