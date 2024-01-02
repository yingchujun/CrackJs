from requests import utils
from curl_cffi import requests


def get_data(page, cookies):

    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0",
    }
    cookies = {
        "sessionid": "bhl4635lwnsywjxq1akwm98f5olihlpx",
    }
    url = "https://match.yuanrenxue.cn/api/match/19"
    params = {
        "page": "{}".format(page)
    }
    response = requests.get(url, headers=headers, cookies=cookies, params=params, impersonate="chrome110")
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
    return utils.dict_from_cookiejar(response.cookies)


if __name__ == '__main__':
    username = ''
    password = ''
    cookies = get_login_cookie(username, password)
    count = 0
    for i in range(1, 6):
        datas = get_data(i, cookies)
        for data in datas:
            count += data['value']
    print(count)