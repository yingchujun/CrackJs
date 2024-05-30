import requests
from requests.utils import dict_from_cookiejar
import execjs
import os

def transferJsCode(fileName, funName,*args):
    jsFilePath = os.path.join(os.path.dirname(__file__), fileName + '.js')
    with open(jsFilePath, mode='r', encoding='utf-8') as f:
        jsCode = f.read() 

    ctx = execjs.compile(jsCode)
    result = ctx.call(funName, *args)
    return result



def login(user, pwd):
    result = transferJsCode('user_pwd', 'encrypt', user, pwd)
    url = 'https://star.endata.com.cn/api/public/login'
    data = {
        'logintype': '1',
        'name': result['user'],
        'pwd': result['pwd']
    }

    response = requests.post(url, data=data)
    return response.cookies



if __name__ == '__main__':
    user = ''
    pwd = ''
    cookie = dict_from_cookiejar(login(user, pwd))
    print(cookie)