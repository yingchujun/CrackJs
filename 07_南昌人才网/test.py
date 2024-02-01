from PIL import Image
import requests
import execjs
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

# 请求获取参数challenge
def challenge():
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0",
    }

    url = "https://www.ncrczpw.com/index.php"
    params = {
        "m": "Home",
        "c": "captcha",
    }
    response = requests.get(url, headers=headers, params=params)
    return response.json()['challenge']

# 获取需要还原和滑块图片URL和随机参数d、e
def data() :
    with open('./enc.js', mode='r', encoding='utf-8') as f:
        jscode = f.read()

    ctx = execjs.compile(jscode)

    # 获取需要还原和滑块的图片数据
    return ctx.call('get_url')

# 底图还原并获取 gapX d e 
def gapX_d_e(): 
    # 获取需要还原和滑块的图片地址
    bg_slice_data = data()

    bg_url = bg_slice_data['bg']
    slice_url = bg_slice_data['slice']

    bg_response = requests.get(bg_url).content
    slice_response = requests.get(slice_url).content
    # 将图片保存
    with open('original.jpg', 'wb') as f1 , open('slice.jpg', 'wb') as f2 :
        f1.write(bg_response)
        f2.write(slice_response)

    # 获取图片裁剪的坐标
    divElm = '''
    <div class="gt_cut_bg gt_show"><div class="gt_cut_bg_slice" style="background-image: url(&quot;https://static.geetest.com/pictures/gt/eccbc87e4/bg/7893487bd.webp&quot;); background-position: -157px -58px;"></div><div class="gt_cut_bg_slice" style="background-image: url(&quot;https://static.geetest.com/pictures/gt/eccbc87e4/bg/7893487bd.webp&quot;); background-position: -145px -58px;"></div><div class="gt_cut_bg_slice" style="background-image: url(&quot;https://static.geetest.com/pictures/gt/eccbc87e4/bg/7893487bd.webp&quot;); background-position: -265px -58px;"></div><div class="gt_cut_bg_slice" style="background-image: url(&quot;https://static.geetest.com/pictures/gt/eccbc87e4/bg/7893487bd.webp&quot;); background-position: -277px -58px;"></div><div class="gt_cut_bg_slice" style="background-image: url(&quot;https://static.geetest.com/pictures/gt/eccbc87e4/bg/7893487bd.webp&quot;); background-position: -181px -58px;"></div><div class="gt_cut_bg_slice" style="background-image: url(&quot;https://static.geetest.com/pictures/gt/eccbc87e4/bg/7893487bd.webp&quot;); background-position: -169px -58px;"></div><div class="gt_cut_bg_slice" style="background-image: url(&quot;https://static.geetest.com/pictures/gt/eccbc87e4/bg/7893487bd.webp&quot;); background-position: -241px -58px;"></div><div class="gt_cut_bg_slice" style="background-image: url(&quot;https://static.geetest.com/pictures/gt/eccbc87e4/bg/7893487bd.webp&quot;); background-position: -253px -58px;"></div><div class="gt_cut_bg_slice" style="background-image: url(&quot;https://static.geetest.com/pictures/gt/eccbc87e4/bg/7893487bd.webp&quot;); background-position: -109px -58px;"></div><div class="gt_cut_bg_slice" style="background-image: url(&quot;https://static.geetest.com/pictures/gt/eccbc87e4/bg/7893487bd.webp&quot;); background-position: -97px -58px;"></div><div class="gt_cut_bg_slice" style="background-image: url(&quot;https://static.geetest.com/pictures/gt/eccbc87e4/bg/7893487bd.webp&quot;); background-position: -289px -58px;"></div><div class="gt_cut_bg_slice" style="background-image: url(&quot;https://static.geetest.com/pictures/gt/eccbc87e4/bg/7893487bd.webp&quot;); background-position: -301px -58px;"></div><div class="gt_cut_bg_slice" style="background-image: url(&quot;https://static.geetest.com/pictures/gt/eccbc87e4/bg/7893487bd.webp&quot;); background-position: -85px -58px;"></div><div class="gt_cut_bg_slice" style="background-image: url(&quot;https://static.geetest.com/pictures/gt/eccbc87e4/bg/7893487bd.webp&quot;); background-position: -73px -58px;"></div><div class="gt_cut_bg_slice" style="background-image: url(&quot;https://static.geetest.com/pictures/gt/eccbc87e4/bg/7893487bd.webp&quot;); background-position: -25px -58px;"></div><div class="gt_cut_bg_slice" style="background-image: url(&quot;https://static.geetest.com/pictures/gt/eccbc87e4/bg/7893487bd.webp&quot;); background-position: -37px -58px;"></div><div class="gt_cut_bg_slice" style="background-image: url(&quot;https://static.geetest.com/pictures/gt/eccbc87e4/bg/7893487bd.webp&quot;); background-position: -13px -58px;"></div><div class="gt_cut_bg_slice" style="background-image: url(&quot;https://static.geetest.com/pictures/gt/eccbc87e4/bg/7893487bd.webp&quot;); background-position: -1px -58px;"></div><div class="gt_cut_bg_slice" style="background-image: url(&quot;https://static.geetest.com/pictures/gt/eccbc87e4/bg/7893487bd.webp&quot;); background-position: -121px -58px;"></div><div class="gt_cut_bg_slice" style="background-image: url(&quot;https://static.geetest.com/pictures/gt/eccbc87e4/bg/7893487bd.webp&quot;); background-position: -133px -58px;"></div><div class="gt_cut_bg_slice" style="background-image: url(&quot;https://static.geetest.com/pictures/gt/eccbc87e4/bg/7893487bd.webp&quot;); background-position: -61px -58px;"></div><div class="gt_cut_bg_slice" style="background-image: url(&quot;https://static.geetest.com/pictures/gt/eccbc87e4/bg/7893487bd.webp&quot;); background-position: -49px -58px;"></div><div class="gt_cut_bg_slice" style="background-image: url(&quot;https://static.geetest.com/pictures/gt/eccbc87e4/bg/7893487bd.webp&quot;); background-position: -217px -58px;"></div><div class="gt_cut_bg_slice" style="background-image: url(&quot;https://static.geetest.com/pictures/gt/eccbc87e4/bg/7893487bd.webp&quot;); background-position: -229px -58px;"></div><div class="gt_cut_bg_slice" style="background-image: url(&quot;https://static.geetest.com/pictures/gt/eccbc87e4/bg/7893487bd.webp&quot;); background-position: -205px -58px;"></div><div class="gt_cut_bg_slice" style="background-image: url(&quot;https://static.geetest.com/pictures/gt/eccbc87e4/bg/7893487bd.webp&quot;); background-position: -193px -58px;"></div><div class="gt_cut_bg_slice" style="background-image: url(&quot;https://static.geetest.com/pictures/gt/eccbc87e4/bg/7893487bd.webp&quot;); background-position: -145px 0px;"></div><div class="gt_cut_bg_slice" style="background-image: url(&quot;https://static.geetest.com/pictures/gt/eccbc87e4/bg/7893487bd.webp&quot;); background-position: -157px 0px;"></div><div class="gt_cut_bg_slice" style="background-image: url(&quot;https://static.geetest.com/pictures/gt/eccbc87e4/bg/7893487bd.webp&quot;); background-position: -277px 0px;"></div><div class="gt_cut_bg_slice" style="background-image: url(&quot;https://static.geetest.com/pictures/gt/eccbc87e4/bg/7893487bd.webp&quot;); background-position: -265px 0px;"></div><div class="gt_cut_bg_slice" style="background-image: url(&quot;https://static.geetest.com/pictures/gt/eccbc87e4/bg/7893487bd.webp&quot;); background-position: -169px 0px;"></div><div class="gt_cut_bg_slice" style="background-image: url(&quot;https://static.geetest.com/pictures/gt/eccbc87e4/bg/7893487bd.webp&quot;); background-position: -181px 0px;"></div><div class="gt_cut_bg_slice" style="background-image: url(&quot;https://static.geetest.com/pictures/gt/eccbc87e4/bg/7893487bd.webp&quot;); background-position: -253px 0px;"></div><div class="gt_cut_bg_slice" style="background-image: url(&quot;https://static.geetest.com/pictures/gt/eccbc87e4/bg/7893487bd.webp&quot;); background-position: -241px 0px;"></div><div class="gt_cut_bg_slice" style="background-image: url(&quot;https://static.geetest.com/pictures/gt/eccbc87e4/bg/7893487bd.webp&quot;); background-position: -97px 0px;"></div><div class="gt_cut_bg_slice" style="background-image: url(&quot;https://static.geetest.com/pictures/gt/eccbc87e4/bg/7893487bd.webp&quot;); background-position: -109px 0px;"></div><div class="gt_cut_bg_slice" style="background-image: url(&quot;https://static.geetest.com/pictures/gt/eccbc87e4/bg/7893487bd.webp&quot;); background-position: -301px 0px;"></div><div class="gt_cut_bg_slice" style="background-image: url(&quot;https://static.geetest.com/pictures/gt/eccbc87e4/bg/7893487bd.webp&quot;); background-position: -289px 0px;"></div><div class="gt_cut_bg_slice" style="background-image: url(&quot;https://static.geetest.com/pictures/gt/eccbc87e4/bg/7893487bd.webp&quot;); background-position: -73px 0px;"></div><div class="gt_cut_bg_slice" style="background-image: url(&quot;https://static.geetest.com/pictures/gt/eccbc87e4/bg/7893487bd.webp&quot;); background-position: -85px 0px;"></div><div class="gt_cut_bg_slice" style="background-image: url(&quot;https://static.geetest.com/pictures/gt/eccbc87e4/bg/7893487bd.webp&quot;); background-position: -37px 0px;"></div><div class="gt_cut_bg_slice" style="background-image: url(&quot;https://static.geetest.com/pictures/gt/eccbc87e4/bg/7893487bd.webp&quot;); background-position: -25px 0px;"></div><div class="gt_cut_bg_slice" style="background-image: url(&quot;https://static.geetest.com/pictures/gt/eccbc87e4/bg/7893487bd.webp&quot;); background-position: -1px 0px;"></div><div class="gt_cut_bg_slice" style="background-image: url(&quot;https://static.geetest.com/pictures/gt/eccbc87e4/bg/7893487bd.webp&quot;); background-position: -13px 0px;"></div><div class="gt_cut_bg_slice" style="background-image: url(&quot;https://static.geetest.com/pictures/gt/eccbc87e4/bg/7893487bd.webp&quot;); background-position: -133px 0px;"></div><div class="gt_cut_bg_slice" style="background-image: url(&quot;https://static.geetest.com/pictures/gt/eccbc87e4/bg/7893487bd.webp&quot;); background-position: -121px 0px;"></div><div class="gt_cut_bg_slice" style="background-image: url(&quot;https://static.geetest.com/pictures/gt/eccbc87e4/bg/7893487bd.webp&quot;); background-position: -49px 0px;"></div><div class="gt_cut_bg_slice" style="background-image: url(&quot;https://static.geetest.com/pictures/gt/eccbc87e4/bg/7893487bd.webp&quot;); background-position: -61px 0px;"></div><div class="gt_cut_bg_slice" style="background-image: url(&quot;https://static.geetest.com/pictures/gt/eccbc87e4/bg/7893487bd.webp&quot;); background-position: -229px 0px;"></div><div class="gt_cut_bg_slice" style="background-image: url(&quot;https://static.geetest.com/pictures/gt/eccbc87e4/bg/7893487bd.webp&quot;); background-position: -217px 0px;"></div><div class="gt_cut_bg_slice" style="background-image: url(&quot;https://static.geetest.com/pictures/gt/eccbc87e4/bg/7893487bd.webp&quot;); background-position: -193px 0px;"></div><div class="gt_cut_bg_slice" style="background-image: url(&quot;https://static.geetest.com/pictures/gt/eccbc87e4/bg/7893487bd.webp&quot;); background-position: -205px 0px;"></div></div>
    '''
    positions = re.findall(r'background-position: (.*?)px (.*?)px;', divElm)
    positions_list = []
    for position in positions:
        x, y  = int(position[0]), int(position[1])
        positions_list.append((x, y))

    # 读取需要还原的图片并将图片设置大小为(260, 116)
    img = Image.open('original.jpg')
    img.resize((260, 116))
    newImg = Image.new(mode='RGB', size=(260, 116)) # 创建一个新图片
    # 底图还原
    for index , position in enumerate(positions_list):

        # 裁剪下第i张图片， 裁剪图片的宽10 长58
        box = (abs(position[0]), abs(position[1]), abs(position[0]) + 10, abs(position[1])+58)
        region = img.crop(box)

        x =  10 * ( index % 26)
        y =  58 * ( index // 26)
        # 第i张图片位置
        newImg.paste(region, (int(x), int(y)))
    newImg.save('restoration.jpg')

    # 缺口x位置
    result = identify_gap('restoration.jpg', 'slice.jpg', 'tip.jpg')
    return {
        'gap': result,
        'd': bg_slice_data['d'],
        'e': bg_slice_data['e']
    }

# 获取验证值
def validate(c, d, e ,challenge) :

    with open('./enc.js', mode='r', encoding='utf-8') as f:
        jscode = f.read()

    ctx = execjs.compile(jscode)

    # 获取validate
    return ctx.call('get_validate',c, d, e ,challenge)



def text(username, password, challenge, validate): 
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0",
    }

    url = "https://www.ncrczpw.com/index.php"
    params = {
        "m": "Home",
        "c": "Members",
        "a": "login"
    }
    data = {
        "username": username,
        "password": password,
        "expire": "1",
        "geetest_challenge": challenge,
        "geetest_validate": validate,
        "geetest_seccode": "{}|jordan".format(validate)
    }
    response = requests.post(url, headers=headers, params=params, data=data)

    print(response.json())

if __name__ == '__main__':
    gap_position = gapX_d_e()
    c = gap_position['gap']
    d = gap_position['d']
    e = gap_position['e']
    challenge = challenge()
    validate = validate(c,d,e,challenge)
    username = ''
    password = ''
    text(username, password, challenge , validate)
