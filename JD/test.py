from io import BytesIO
from PIL import Image
import requests
import execjs
import cv2
import time

with open('./test.js', 'r', encoding='utf-8') as f:
    js_code = f.read()
ctx = execjs.compile(js_code)


headers = {
    'Origin': 'https://login.dangdang.com',
    'Referer': 'https://login.dangdang.com/?returnurl=https%3A%2F%2Fwww.dangdang.com%2F',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
}




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

# 调整底图大小并保存
def resize_and_save_image(path ,content, size):
    image = Image.open(BytesIO(content))
    image = image.resize(size)
    image.save(path)


def ranKey(data):
    url = "https://login.dangdang.com/api/customer/loginapi/getRankey"
    response = requests.post(url, headers=headers, data=data)
    return response.json()

def getSlidingVerifyCode(data):
    url = "https://login.dangdang.com/api/customer/loginapi/getSlidingVerifyCode"
    response = requests.post(url, headers=headers, data=data)
    print(response.json())
    return response.json()

def save_captcha_img(url):
    response = requests.get(url, headers=headers)
    return response.content

def checkSlidingVerifyCode(data3):


    data = {
        't': data3['t'],
        'ct': 'pc',
        'permanent_id': data3['permanent_id'],
        'requestId': data3['requestId'],
        'situation': 'login',
        'verifyToken': data3['verifyToken'],
        'slide_cost_time': '77',
        'need_new_verifydata': '0',
        'point_json': data3['point_json'],
        'sign': data3['sign'],
    }

    response = requests.post('https://login.dangdang.com/api/customer/loginapi/checkSlidingVerifyCode', headers=headers, data=data)
    print(response.json())
    return response.json()

def accountLogin(data4):
    data = {
        't': data4['t'],
        'ct': 'pc',
        'permanent_id': data4['permanent_id'],
        'requestId': data4['requestId'],
        'username': data4['username'],
        'password': data4['password'],
        'autokey': 'off',
        'token': data4['verifyToken'],
        'check_code': data4['check_code'],
        'check_code_type': '1',
        'sign': data4['sign'],
    }

    response = requests.post('https://login.dangdang.com/api/customer/loginapi/accountLogin',headers=headers,data=data)
    print(response.json())

if __name__ == '__main__':
    username = ''
    password = ''
    password = ctx.call('password', password)

    # t 、 ct 、 requestId 、 sign 、 permanent_id
    # 第一次请求data
    data = ctx.call('params')
    permanent_id = data['permanent_id']
    requestId = data['requestId']
    ranKey = ranKey(data) # requestId 
    print(data, ranKey)
    # 第二次请求data
    data2 = ctx.call('params', ranKey['rankey'], ranKey['requestId'], 'login')
    result = getSlidingVerifyCode(data2)
    slideImg = save_captcha_img(result['data']['slideImg'])
    bgImg = save_captcha_img(result['data']['bgImg'])
    encryptKey = result['data']['encryptKey']
    verifyToken = result['data']['token']
    y = result['data']['y']

    resize_and_save_image('./slideImg.png', slideImg, (61,61))
    resize_and_save_image('./bgImg.jpg', bgImg, (350,175))

    x = identify_gap('./bgImg.jpg', './slideImg.png', './out.png')
    point_json = ctx.call("point_json", x, y, encryptKey)
    data3 = ctx.call('params', ranKey['rankey'], ranKey['requestId'], 'login', permanent_id, point_json, verifyToken)
    data3['verifyToken'] = verifyToken
    data3['point_json'] = point_json
    check_code = checkSlidingVerifyCode(data3)['data']['checkCode']


    data4 = ctx.call('params', ranKey['rankey'], ranKey['requestId'], '', permanent_id, '', verifyToken, check_code, password, username)
    data4['username'] = username
    data4['check_code'] = check_code
    data4['verifyToken'] = verifyToken
    data4['password'] = password
    accountLogin(data4)
