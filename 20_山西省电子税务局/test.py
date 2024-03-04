from io import BytesIO
from PIL import Image
import requests
import base64
import execjs
import time
import json
import cv2



# 调整底图大小并保存
def resize_and_save_image(path ,content, size):
    image = Image.open(BytesIO(content))
    image = image.resize(size)
    image.save(path)

# 判断缺口位置 返回缺口的X坐标
def identify_gap(bg,tp,out):
    '''
    bg: 背景图片
    tp: 缺口图片
    out:输出图片
    '''
    # 读取背景图片和缺口图片
    bg_img = cv2.imread(bg) # 背景图片
    tp_img = cv2.imread(tp) # 缺口图片
    
    # 识别图片边缘
    bg_edge = cv2.Canny(bg_img, 100, 200)
    tp_edge = cv2.Canny(tp_img, 100, 200)
    
    # 转换图片格式
    bg_pic = cv2.cvtColor(bg_edge, cv2.COLOR_GRAY2RGB)
    tp_pic = cv2.cvtColor(tp_edge, cv2.COLOR_GRAY2RGB)
    
    # 缺口匹配
    res = cv2.matchTemplate(bg_pic, tp_pic, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res) # 寻找最优匹配
    
    # 绘制方框
    th, tw = tp_pic.shape[:2] 
    tl = max_loc # 左上角点的坐标
    br = (tl[0]+tw,tl[1]+th) # 右下角点的坐标
    cv2.rectangle(bg_img, tl, br, (0, 0, 255), 2) # 绘制矩形
    cv2.imwrite(out, bg_img) # 保存在本地
    
    # 返回缺口的X坐标
    return tl[0] 

# 获取验证码参数
def verifyParams():
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 Edg/122.0.0.0",
    }
    url = "https://etax.shanxi.chinatax.gov.cn/gzfw/common/captcha/get"
    data = {
        "captchaType": "blockPuzzle",
        "clientUid": "slider-b1faba8f-805c-4cf4-8584-e9cb1d006340",
    }
    data = json.dumps(data, separators=(',', ':'))
    return requests.post(url, headers=headers, data=data).json()['repData']

# 滑块验证码验证
def check(token, pointJson):
    headers = {
        "Accept": "*/*",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        "Content-Type": "application/json;charset=UTF-8",
        "Origin": "https://etax.shanxi.chinatax.gov.cn",
        "Pragma": "no-cache",
        "Referer": "https://etax.shanxi.chinatax.gov.cn/gzfw/xydjalnsrcx",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 Edg/122.0.0.0",
        "sec-ch-ua": "\"Chromium\";v=\"122\", \"Not(A:Brand\";v=\"24\", \"Microsoft Edge\";v=\"122\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\""
    }
    cookies = {
    }
    url = "https://etax.shanxi.chinatax.gov.cn/gzfw/common/captcha/check"
    data = {
        "captchaType": "blockPuzzle",
        "pointJson": pointJson,
        "token": token,
        "clientUid": "slider-b1faba8f-805c-4cf4-8584-e9cb1d006340",
        "ts": int(time.time()*1000)
    }
    data = json.dumps(data, separators=(',', ':'))

    requests.post(url, headers=headers, cookies=cookies, data=data)

# 数据请求
def getData(captchaVerification, nsrsbh, nsrmc):
    headers = {
        "Referer": "https://etax.shanxi.chinatax.gov.cn/gzfw/xydjalnsrcx",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 Edg/122.0.0.0",
    }
    url = "https://etax.shanxi.chinatax.gov.cn/gzfw/xydjalnsrcx/list"
    params = {
        "captchaVerification": captchaVerification,
        "_search": "false",
        "nd": int(time.time()*1000),
        "limit": "50",
        "page": "1",
        "sidx": "",
        "sord": "asc",
        "CXLX": "0",
        "NSRSBH": nsrsbh,
        "NSRMC": nsrmc,
        "ZGSWJ": "",
        "ZGSWJ_DM": "",
        "TYPE": "0",
        "DJXH": "",
        "YEAR": "2023"
    }
    response = requests.get(url, headers=headers, params=params)
    print(response.json())

# 测试
if __name__ == '__main__':
    # 纳税人识别号
    nsrsbh = ''
    # 纳税人名称
    nsrmc = ''

    result = verifyParams()
    bg = result['originalImageBase64']
    slide = result['jigsawImageBase64']
    secretKey = result['secretKey']
    token = result['token']
    bg_data = base64.b64decode(bg)
    slide_data = base64.b64decode(slide)
    # 重置图片大小
    resize_and_save_image('base.png', bg_data, (400, 200))
    resize_and_save_image('slide.png', slide_data, (60, 200))

    # 获取缺口x轴位置
    x = identify_gap('base.png', "slide.png", 'out.png') * 310 / 400

    with open('./Verification.js', mode='r', encoding='utf-8') as f:
        js_code = f.read()

    ctx = execjs.compile(js_code)
    pointJson = ctx.call('pointJson',x, secretKey)
    captchaVerification = ctx.call('captchaVerification', token, x, secretKey)

    check(token, pointJson)
    getData(captchaVerification, nsrsbh, nsrmc)
    

