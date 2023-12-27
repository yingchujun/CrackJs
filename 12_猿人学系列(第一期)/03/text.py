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


def get_data(page,cookie=''):

    session = requests.session()
    session.headers = {
        'Host': 'match.yuanrenxue.cn',
        'Connection': 'keep-alive',
        'Content-Length': '0',
        'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Microsoft Edge";v="120"',
        'sec-ch-ua-mobile': '?0',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0',
        'sec-ch-ua-platform': "Windows",
        'Accept': '*/*',
        'Origin': 'https://match.yuanrenxue.cn',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://match.yuanrenxue.cn/match/3',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Cookie': 'sessionid={}'.format(cookie),

    }


    jssm_url = "https://match.yuanrenxue.cn/jssm"
    session.post(jssm_url)

    data_url = 'https://match.yuanrenxue.cn/api/match/3?page={}'.format(page)
    response = session.post(data_url)
    return response.json()['data']



if __name__ == '__main__':
    username = ''
    password = ''
    cookies = get_login_cookie(username, password)
    result = get_data(1, cookies['sessionid'])
    query = {}
    maxCount = 1
    mostMum = ''
    for _ in range(1, 6):
        for item in result:
            curNum = item['value']
            if curNum not in query:
                query[curNum] = 1
            else:
                query[curNum] += 1
            if query[curNum] >= maxCount:
                maxCount = query[curNum]
                mostMum = curNum
    print(mostMum)
