import requests
import execjs
import json

def get_enc_data(page):

    headers = {
        "Referer": "https://jzsc.mohurd.gov.cn/data/company",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0",
    }

    url = "https://jzsc.mohurd.gov.cn/APi/webApi/dataservice/query/comp/list"
    params = {
        "pg": "{}".format(page),
        "pgsz": "15",
        "total": "450"
    }
    response = requests.get(url, headers=headers, params=params)

    return response.text

def get_dec_data(enc_data):
    with open('./data.js', mode='r', encoding='utf-8') as f:
        js_code = f.read()
    ctx = execjs.compile(js_code)
    result = ctx.call('dec_data', enc_data)
    print(json.loads(result))

if __name__ == '__main__':
    enc_data = get_enc_data(1)
    dec_data = get_dec_data(enc_data)
    print(dec_data)