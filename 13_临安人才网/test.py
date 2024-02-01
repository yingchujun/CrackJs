import os 
import re
import execjs
import requests
from lxml import etree
 
url = "https://www.lazpw.cn/job"
params = {
    "keyword_type": "1",
    "page": "1"
}

def first_req_get_arg2() :

    response = requests.get(url, params=params)
    arg1 = re.findall("var arg1='(.*?)';", response.text)[0]

    cur_path = os.path.dirname(__file__)
    with open(os.path.join(cur_path, 'enc.js'), mode='r', encoding='utf-8') as f:
        js_code = f.read()  
    ctx = execjs.compile(js_code)
    arg2 = ctx.call('arg2', str(arg1))
    return arg2


def second_req_get_data():
    cookie = {
        'acw_sc__v2': first_req_get_arg2()
    }
    response = requests.get(url, cookies=cookie, params=params)
    html = etree.HTML(response.text)
    divs = html.xpath("//div[@class='saith']")
    for div in divs:
        title = div.xpath(".//li[@class='list1']/a/text()")[0]
        salary = div.xpath(".//li[@class='list2']/text()")[0]
        company_name = div.xpath(".//li[@class='list4']/a/text()")[0]
        print([title, salary, company_name])


if __name__ == '__main__':
    second_req_get_data()
