import requests
import execjs
import json

with open('./18_唯品会/mars_cid.js', mode='r', encoding='utf-8') as f:
    js_code = f.read()

ctx = execjs.compile(js_code)
mars_cid = ctx.call('mars_cid')


headers = {
    "referer": "https://category.vip.com/",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0"
}
url = "https://mapi.vip.com/vips-mobile/rest/shopping/pc/search/product/rank"
params = {
    "app_name": "shop_pc",
    "app_version": "4.0",
    "warehouse": "VIP_SH",
    "fdc_area_id": "103103102",
    "client": "pc",
    "mobile_platform": "1",
    "province_id": "103103",
    "api_key": "70f71280d5d547b2a7bb370a529aeea1",
    "user_id": "",
    "mars_cid": mars_cid,
    "wap_consumer": "a",
    "standby_id": "nature",
    "keyword": "python",
    "lv3CatIds": "",
    "lv2CatIds": "",
    "lv1CatIds": "",
    "brandStoreSns": "",
    "props": "",
    "priceMin": "",
    "priceMax": "",
    "vipService": "",
    "sort": "0",
    "pageOffset": "0",
    "channelId": "1",
    "gPlatform": "PC",
    "batchSize": "120",
}


response = requests.get(url, headers=headers,  params=params)
print(json.loads(response.text))