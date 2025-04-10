import json

import requests

from setting import test_url


def login(username,password):
    payload = json.dumps({
        "password": password,
        "isCookie": False,
        "captchaType": 1,
        "account": username
    })
    headers = {
        'User-Agent': 'Apifox/1.0.0 (https://apifox.com)',
        'Content-Type': 'application/json',
        'Accept': '*/*',
        'Host': '172.17.25.223:80',
        'Connection': 'keep-alive'
    }
    print(payload)
    response = requests.request("POST", test_url+'/login', headers=headers, data=payload)

    print(response.json())
    return response.json()