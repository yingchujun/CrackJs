import requests
import json
import execjs 
import os


def cst():
    with open(os.path.join(os.path.dirname(__file__), 'slideToken.js'), mode='r', encoding='utf-8') as f:
        js_code = f.read()

    ctx = execjs.compile(js_code)
    res = ctx.call('slider')

    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0"
    }
    url = "https://vercode.qunar.com/inner/captcha/snapshot"
    data = {
        "data": res,
        "orca": 2,
        "appCode": "register_pc",
        "cs": "pc"
    }
    data = json.dumps(data, separators=(',', ':'))
    cst = requests.post(url, headers=headers, data=data).json()['data']['cst']
    return cst 


def login(username , password ,cst):
    url = "https://user.qunar.com/weblogin/password"
    headers = {
        "content-type": "application/json;charset=UTF-8",
        "origin": "https://user.qunar.com",
        "referer": "https://user.qunar.com/passport/login.jsp?ret=https%3A%2F%2Fwww.qunar.com%2F",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0"
    }
    data = {
        "piccoloT": "login_register_pc",
        "username": username,
        "password": password,
        "prenum": "86",
        "type": "3",
        "source": "",
        "remember": True,
        "slideToken": cst,
        "appcode": "register_pc",
        "loginSource": 1,
        "captchaType": "",
        "usersource": "",
        "ret": "https://www.qunar.com/",
        "ref": "",
        "business": "",
        "pid": "",
        "originChannel": "",
        "activityCode": ""
    }



    data = json.dumps(data, separators=(',', ':'))
    response = requests.post(url, headers=headers, data=data)
    print(response.cookies)


# test
if __name__ == '__main__':
    username = ''
    password = ''
    cst = cst()
    login(username, password, cst)