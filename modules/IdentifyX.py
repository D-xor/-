import cv2
import numpy as np
import math 

def showimg(img):
    cv2.imshow('Marked Image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def get_top_bottom(img):
    # gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # 应用Canny边缘检测
    edges = cv2.Canny(img, 50, 150, apertureSize=7, L2gradient=True)

    # 查找轮廓
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    # 假设最大的轮廓是滑块的轮廓
    max_contour = max(contours, key=cv2.contourArea)
    x, y, w = cv2.minAreaRect(max_contour)
    # 计算轮廓的边界框
    top_height = int(x[1] - 46)
    bottom_height = int(x[1] + 46)
    return top_height, bottom_height

def get_img(img_path):
    with open(img_path, 'rb') as b:
        img = b.read()
    
    cv2_img = cv2.imdecode(np.frombuffer(img, np.uint8), cv2.IMREAD_GRAYSCALE)

    return cv2_img

def identify_edge(img, mode=1):
    if mode == 1:
        img_edge = cv2.Canny(img, 300, 800)
    elif mode == 2:
        img_edge = cv2.Canny(img, 300, 600)
    elif mode == 3:
        img_edge = cv2.Canny(img, 200, 400, L2gradient=True)
    elif mode == 0:
        img_edge = cv2.Canny(img, 400, 800, L2gradient=True)

    # 转换图片格式
    img_pic = cv2.cvtColor(img_edge, cv2.COLOR_GRAY2RGB)
    
    return img_pic

def match_edge(bg_edge, slider_edge):
    res = cv2.matchTemplate(bg_edge, slider_edge, cv2.TM_CCORR)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)  # 寻找最优匹配
    return max_loc

def traditional_round(number, ndigits=0):
    '''返回数字的四舍五入值'''
    factor = 10 ** ndigits
    round_num = math.floor(number * factor + 0.5) / factor if number > 0 else math.ceil(number * factor - 0.5) / factor
    return int(round_num)


def get_x():
    bg_img, slider_img = get_img("./imgs/_big.jpg"), get_img("./imgs/_puzzle.jpg")
    # 获取上高下高
    top_y, bottom_y = get_top_bottom(slider_img)
    # 灰度处理等操作
    bg_edge = identify_edge(bg_img, mode=1)
    slider_edge = identify_edge(slider_img, mode=0)
    # 截取掉无关区域
    bg_edge = bg_edge[top_y:bottom_y, :]
    slider_edge = slider_edge[top_y:bottom_y, :]
    # 匹配边缘
    matched_result = match_edge(bg_edge, slider_edge)    
    mode_num = 1
    while matched_result[1] < 50:
        mode_num += 1
        matched_result = match_edge(identify_edge(bg_img, mode=mode_num), slider_edge)
        if mode_num >= 3:
            break

    tl = matched_result  # 左上角点的坐标
    th, tw = slider_edge.shape[:2]
    br = (tl[0] + tw, tl[1] + th)  # 右下角点的坐标
    cv2.rectangle(bg_img, tl, br, (0, 0, 255), 2)  # 绘制矩形
    cv2.imwrite('./imgs/mark.jpg', bg_img)  # 保存在本地
    # 返回缺口的X坐标
    x = traditional_round(matched_result[0] * 0.5833)  # 480x270 -> 280x158
    # x = max_loc[0]
    return x


if __name__ == '__main__':
    x = get_x()
    print(x)



