from requests.utils import dict_from_cookiejar
from lxml import etree
import requests
import ddddocr
import random
import re

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 Edg/122.0.0.0",
}

def get_verify_params():
    url = "https://passport.yougou.com/signin.jhtml"
    params = {
        "redirectURL": "https://www.yougou.com/"
    }
    response = requests.get(url, headers=headers, params=params)
    html = etree.HTML(response.text)
    name = html.xpath('//input[@id="loginNonceId"][1]/@name')[0]
    value = html.xpath('//input[@id="loginNonceId"][1]/@value')[0]
    cookie = dict_from_cookiejar(response.cookies)
    cookie.update({'name' : name, 'value': value})
    return cookie


def login(cookie, verifycode, name, value, username, password):

    url = "https://passport.yougou.com/my/procsignin.jhtml"
    params = {
        "callback": "jsonp1710471508260"
    }
    data = {
        "username": username,
        "password": password,
        "verifycode": verifycode,
        "isVerify": "true",
        name: value,
        "callback": "jsonp1710471508260"
    }
    response = requests.post(url, headers=headers, cookies=cookie, params=params, data=data)
    message = re.findall('\((.*?)\)', response.text)[0]
    print(message)


def get_verify_code(cookies):

    url = "https://passport.yougou.com/servlet/imageCaptcha"
    params = {
        "rand": random.random()
    }
    response = requests.get(url, headers=headers, cookies=cookies, params=params)
    # with open('./verifyImg.png', 'wb') as f:
    #     f.write(response.content)

    ocr = ddddocr.DdddOcr()
    res = ocr.classification(response.content)
    return res

# 测试
if __name__ == '__main__':
    username = ''
    password = ''
    verify_params = get_verify_params()
    cookie = {
        'yg_sid' : verify_params['yg_sid'],
        'JSESSIONID' : verify_params['JSESSIONID']
    }
    verifycode = get_verify_code(cookie)
    login(cookie, verifycode, verify_params['name'], verify_params['value'], username, password)