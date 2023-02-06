import requests
try:

    res = requests.get(f'http://127.0.0.1:5000/api/users/userData/1')
    if res.ok:
        print(res.json())
    elif res.status_code==404:
        raise Exception("Empty user line")
except Exception as y:
    print(y)   