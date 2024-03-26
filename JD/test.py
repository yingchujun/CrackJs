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
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 Edg/122.0.0.0",
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
    return response.json()

def save_captcha_img(url):
    response = requests.get(url, headers=headers)
    return response.content

def checkSlidingVerifyCode(t, permanent_id, requestId,verifyToken, point_json):


    data = {
        't': t,
        'ct': 'pc',
        'permanent_id': permanent_id,
        'requestId': requestId,
        'situation': 'login',
        'verifyToken': verifyToken,
        'slide_cost_time': '883',
        'need_new_verifydata': '0',
        'point_json': point_json,
    }

    response = requests.post('https://login.dangdang.com/api/customer/loginapi/checkSlidingVerifyCode', headers=headers, data=data)
    print(response.json())

if __name__ == '__main__':
    # t 、 ct 、 requestId 、 sign 、 permanent_id
    # 第一次请求data
    data = ctx.call('params')
    permanent_id = data['permanent_id']
    requestId = data['requestId']
    ranKey = ranKey(data) # requestId 
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
    t = int(time.time()*1000)
    checkSlidingVerifyCode(t, permanent_id, requestId,verifyToken, point_json)

    
