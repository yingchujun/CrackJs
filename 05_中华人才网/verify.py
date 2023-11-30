import requests
from lxml import etree
import cv2
import requests
import base64
from PIL import Image
from io import BytesIO
import time
import random
import re


# 缺口识别
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




headers = {
    "X-Requested-With": "XMLHttpRequest",
}
url = "http://www.zhrc.com/CompanyDetail.aspx"

params = {
    "id": "73679"
}
response = requests.get(url, headers=headers, params=params, verify=False, allow_redirects=False)

if 'Object moved to' in response.text:
    print('开始验证')
    html = etree.HTML(response.text)
    verify_url = html.xpath('//h2/a/@href')[0]
    k = re.findall('k=(.*?)&', verify_url)[0]
    url = "https://swx.qzrc.com/System/MakeBLCode"
    data = {
        "key": k
    }
    response = requests.post(url, headers=headers, data=data).json()
    crop_picture  = base64.b64decode(response['Data']['normal'].split(',')[1])
    slider_picture = base64.b64decode(response['Data']['small'].split(',')[1])
    crop_data = BytesIO(crop_picture)
    slider_data = BytesIO(slider_picture)
    # 图片大小
    imgx = response['Data']['imgx']
    imgy = response['Data']['imgy']
    # 裁剪后每个图片的大小
    cutX = imgx / 10;
    cutY = imgy / 2;
    # 混淆图片位置数组
    bgarray = response['Data']['array'].split(',')

    slider = Image.open(slider_data)
    img = Image.open(crop_data)
    newImg = Image.new(mode='RGB', size=(imgx, imgy)) # 创建一个新图片

    # 底图还原
    for i in range(20):
        position = bgarray.index(str(i))
        topLeftX = cutX * (position % 10)
        topLeftY = cutY * (position // 10)
        bottomRightX = cutX * (position % 10 + 1 )
        bottomRightY = cutY * (position // 10 + 1)
        # 前两个坐标点是左上角坐标
        # 后两个坐标点是右下角坐标
        # width在前， height在后
        # 裁剪下第i张图片
        box = (int(topLeftX), int(topLeftY), int(bottomRightX), int(bottomRightY))
        region = img.crop(box)

        # 第i张图片位置
        newImg.paste(region, (int(cutX * (i  % 10)), int(cutY * (i // 10))))

    slider.save('slider.jpg')
    # img.save('还原前.jpg')
    newImg.save('restoration.jpg')

    sliderX = identify_gap('restoration.jpg', 'slider.jpg', 'tip.jpg')
    print(sliderX)
    timeStart = int(time.time()*1000)
    start = 1
    datelist = ''
    #  轨迹模拟
    while start < sliderX:
        point = str(start) + ',' + str(int(time.time()*1000))
        datelist += point + '|' 
        start += random.randint(1,5)
    datelist += str(sliderX) + ',' + str(int(time.time()*1000))

    timeEnd = int(time.time()*1000)
    timespan = timeEnd - timeStart

    url = "https://swx.qzrc.com/System/CheckBLCode"
    data = {
        "key": f"{k}",
        "point": f"{sliderX}",
        "timespan": f"{timespan}",
        "datelist": f"{datelist}"
    }
    response = requests.post(url, headers=headers, data=data).json()
    if response['Code'] == 0:
        url = "http://www.zhrc.com/CompanyDetail.aspx"
        params = {
            "id": "73679"
        }
        response = requests.get(url, headers=headers, params=params, verify=False, allow_redirects=False)
        print(response.text)
    else:
        print('验证失败')

else:
    print('无需验证')