import requests
import os
import execjs

curFilePath = os.path.dirname(os.path.abspath(__file__))
def get_data(page, m, t, cookies):

    url = "https://match.yuanrenxue.cn/api/match/16"
    params = {
        "page": str(page),
        "m": m,
        "t": t
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
    with open(os.path.join(curFilePath, 'text.js'), mode='r', encoding='utf-8') as f:
        jsCode = f.read()
    ctx = execjs.compile(jsCode)
    result = ctx.call('m')
    return result
    
if __name__ == '__main__':
    username = ''
    password = ''
    cookies = get_login_cookie(username, password)
    count = 0
    print()
    for i in range(1, 6):
        result = get_m()
        m = result['m']
        t = result['t']
        datas = get_data(i, m, t, cookies)
        for data in datas:
            count += data['value']
    print(count)