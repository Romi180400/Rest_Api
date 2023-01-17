import requests

try:

    res = requests.get('http://127.0.0.1:5000/stop_server')
    if res.ok:
        print("Rest Server is terminated")
except Exception as y:
    print(y)   


try:
    
    res = requests.get('http://127.0.0.1:5001/stop_server')
    if res.ok:
        print("Web app is terminated")
except Exception as x:
    print(x)   