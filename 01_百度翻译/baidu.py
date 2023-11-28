import requests
import execjs
import re
import os

current_path = os.path.dirname(os.path.abspath(__file__))
enc_jd_path = os.path.join(current_path, 'sign.js')
ctx = execjs.compile(open(enc_jd_path, encoding='utf-8').read())

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0",
}
# 首页获取gtk和token
index_url = 'https://fanyi.baidu.com/'
response = requests.get(index_url, headers=header)
first_cookie = requests.utils.dict_from_cookiejar(response.cookies)
# 需要携带第一次请求返回的ck再次请求首页获取token否则首页token为空
response = requests.get(index_url, headers=header, cookies=first_cookie)
token = re.findall("token: \'(.*?)\'\,", response.text)[0]
gtk = re.findall('gtk = "(.*?)";', response.text)[0]


query = 'python'
sign = ctx.call('sign', query, gtk)

# 翻译接口
trans_api_url = "https://fanyi.baidu.com/v2transapi"
data = {
    "from": "en",
    "to": "zh",
    "query": query,
    "transtype": "enter",
    "simple_means_flag": "3",
    "sign": sign,
    "token": token,
    "domain": "common",
}
response = requests.post(trans_api_url, headers=header, cookies=first_cookie, data=data)

print(response.json())