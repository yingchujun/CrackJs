import requests
import pywasm
import os
import time
import random
import math


curFilePath = os.path.dirname(os.path.abspath(__file__))
def get_data(page,m,cookies):

    url = "https://match.yuanrenxue.cn/api/match/15"
    params = {
        "m": m,
        "page": str(page)
    }
    response = requests.get(url, cookies=cookies, params=params)
    return response.json()['data']

# 获取登录ck
def get_login_cookie(username, password):
    login_url = 'https://match.yuanrenxue.cn/api/login'
    data = {
        'username': username,
        'password': password
    }
    response = requests.post(login_url, data=data)
    print(response.json()['message'])
    return requests.utils.dict_from_cookiejar(response.cookies)


def get_m():
    t1 = int(time.time()/2)
    t2 = int(time.time()/2) - math.floor(random.random() * 50 + 1)

    curFilePath = os.path.dirname(os.path.abspath(__file__))
    runtime = pywasm.load(os.path.join(curFilePath, 'main.wasm'))
    result = runtime.exec('encode', [t1,t2])
    return str(result) + '|' + str(t1) + "|" + str(t2)

if __name__ == '__main__':
    username = '1324827156'
    password = '180611sxy'
    cookies = get_login_cookie(username, password)
    count = 0
    for i in range(1, 6):
        m = get_m()
        datas = get_data(i, m, cookies)
        for data in datas:
            count += data['value']
    print(count)