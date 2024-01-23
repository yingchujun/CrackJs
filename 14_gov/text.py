import os 
import re
import execjs
import requests
from lxml import etree
from requests.utils import dict_from_cookiejar


url = 'https://www.mps.gov.cn/n2254098/n4904352/index_3497341_74.html'
headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Referer": "https://www.mps.gov.cn/n2254098/n4904352/index_3497341_74.html",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0",
}
cur_path = os.path.dirname(__file__)

def first_req():
    response = requests.get(url, headers=headers)
    cookies = dict_from_cookiejar(response.cookies)
    cookies['__jsl_clearance_s'] = execjs.eval(re.findall('\(.*\)', response.text)[0]).split(';')[0].split('=')[1]
    return cookies


def second_req():
    cookies = first_req()
    response = requests.get(url, cookies=cookies, headers=headers)
    html = etree.HTML(response.text)
    enc_code = html.xpath('//script/text()')[0]

    with open(os.path.join(cur_path, 'enc.js'), mode='r', encoding='utf-8') as f:
        js_code = f.read()
        
    ctx = execjs.compile(js_code)
    __jsl_clearance_s = ctx.call('jsl_clearance_s', enc_code)
    cookies['__jsl_clearance_s'] = __jsl_clearance_s.split(';')[0].split('=')[1]
    return  cookies


def third_req():
    cookies = second_req()
    response = requests.get(url, cookies=cookies, headers=headers)
    response.encoding = response.apparent_encoding
    html = etree.HTML(response.text)
    dds = html.xpath('//dd/a/text()')
    for dd in dds:
        print(dd)

third_req()