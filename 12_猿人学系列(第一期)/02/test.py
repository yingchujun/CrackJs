import requests
import execjs
import os 

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
    file_path = os.path.join(os.path.dirname(__file__), 'm.js')
    with open(file_path, mode='r', encoding='utf-8') as f:
        js_code = f.read()
    ctx = execjs.compile(js_code)
    m = ctx.call('get_m')
    return m

def get_data(page,cookie={}):
    headers = {
        "referer": "https://match.yuanrenxue.cn/match/2",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0",
    }
    url = "https://match.yuanrenxue.cn/api/match/2"
    params = {
        'page': page,
    }
    response = requests.get(url, headers=headers, cookies=cookie, params=params)
    return response.json()['data']


if __name__ == '__main__':
    username = ''
    password = ''
    cookies = get_login_cookie(username, password)
    cookies.update({'m': get_m()})
    count = 0
    for i in range(5):
        result = get_data(i+1, cookies)
        for item in result:
            count += item['value']
    
    print(count )
