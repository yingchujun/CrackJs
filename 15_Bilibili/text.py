import os 
import time 
import execjs
import requests




def get_enc_params():

    time_now = int(time.time() * 1000)
    headers = {
        "origin": "https://space.bilibili.com",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0"
    }
    url = "https://passport.bilibili.com/x/passport-login/web/key"
    params = {
        "_": str(time_now)
    }
    response = requests.get(url, headers=headers,  params=params)
    return response.json()["data"]

def get_enc_pwd(pwd):

    enc_params = get_enc_params()
    key = enc_params['key']
    hash = enc_params['hash']
    cur_path = os.path.dirname(__file__)

    with open(os.path.join(cur_path, 'password.js'), mode='r',  encoding='utf-8') as f:
        js_code = f.read()
    
    ctx = execjs.compile(js_code)
    result = ctx.call('password', key, hash, pwd)
    print(result)
    return result

get_enc_pwd('123456')