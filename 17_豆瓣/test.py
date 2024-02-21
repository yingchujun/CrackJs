from io import BytesIO
from PIL import Image
import requests
import base64
import json
import cv2
import re

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

# 将滑块从精灵图中裁剪下来
def crop_sprite_to_slide(sprite):
    image = Image.open(BytesIO(sprite))
    image = image.resize((282, 256))
    cropped = image.crop((58, 203, 58+49, 203+49))
    cropped.save("slide.png")

# 调整底图大小并保存
def resize_and_save_image(path ,content):
    image = Image.open(BytesIO(content))
    image = image.resize((278, 161))
    image.save(path)


def get_tc_app_id():

    headers = {
        "Referer": "https://accounts.douban.com/passport/login_popup?login_source=anony",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0"
    }
    url = "https://accounts.douban.com/j/mobile/login/basic"
    data = {
        "remember": "true",
        "name": "15858585858",
        "password": "123456"
    }

    response = requests.post(url, headers=headers, data=data)

    return response.json()['payload']['tc_app_id']

def get_captcha_params(tc_app_id, user_agent): 
    headers = {
        "Referer": "https://accounts.douban.com/",
        "User-Agent": user_agent,
    }
    url = "https://turing.captcha.qcloud.com/cap_union_prehandle"
    params = {
        "aid": tc_app_id,
        "protocol": "https",
        "accver": "1",
        "showtype": "popup",
        "ua": base64.b64encode(user_agent.encode()).decode(),
        "noheader": "1",
        "fb": "1",
        "aged": "0",
        "enableAged": "0",
        "enableDarkMode": "0",
        "grayscale": "1",
        "clientype": "2",
        "cap_cd": "",
        "uid": "",
        "lang": "zh-cn",
        "entry_url": "https://accounts.douban.com/passport/login_popup",
        "elder_captcha": "0",
        "js": "/tcaptcha-frame.22125576.js",
        "login_appid": "",
        "wb": "1",
        "subsid": "11",
        "sess": ""
    }

    response = requests.get(url, headers=headers, params=params)
    data = json.loads(re.findall('\((.*?)\)', response.text)[0])
    return dict(data)

def save_captcha_img(url):
    headers = {
        "Referer": "https://turing.captcha.gtimg.com/",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0",
    }
    response = requests.get(url, headers=headers)
    return response.content



if __name__ == '__main__':
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0"
    captcha_params = get_captcha_params(get_tc_app_id(), user_agent)
    sess = captcha_params['sess']
    img_url = 'https://turing.captcha.qcloud.com' + captcha_params['data']['dyn_show_info']['bg_elem_cfg']['img_url']
    sprite_url = 'https://turing.captcha.qcloud.com' + captcha_params['data']['dyn_show_info']['sprite_url']
    base_map = save_captcha_img(img_url)
    resize_and_save_image('base.png', base_map)

    # 获取滑块
    sprite_map = save_captcha_img(sprite_url)
    crop_sprite_to_slide(sprite_map)
    x = identify_gap('base.png', "slide.png", 'out.png')
    print(x)
