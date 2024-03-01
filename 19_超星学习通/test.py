import requests
import execjs

with open('./user_pwd.js', mode='r', encoding='utf-8') as f:
    jsCode = f.read()

ctx = execjs.compile(jsCode)
result = ctx.call('enc', '123456', '15858585858')
uname = result['phone']
password = result['pwd']
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 Edg/122.0.0.0",
}

url = "https://passport2.chaoxing.com/fanyalogin"
data = {
    "fid": "-1",
    "uname": uname,
    "password": password,
    "refer": "http%3A%2F%2Fi.mooc.chaoxing.com",
    "t": "true",
    "forbidotherlogin": "0",
    "validate": "",
    "doubleFactorLogin": "0",
    "independentId": "0",
    "independentNameId": "0"
}
response = requests.post(url, headers=headers, data=data)

print(response.json())