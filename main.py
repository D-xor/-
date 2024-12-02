"""安居客滑块 2023-07-06"""

import re
import execjs
import requests
from modules.IdentifyX import get_x
from modules.BezierTrack import get_track
from settings import *
from PyLogger import MyLogger



# 获取sessionId
def get_sessionId():
    resp = requests.get(url=sessionId_api, headers=UserAgent)
    if resp.status_code == 200:
        sessionId = re.findall("sessionId:\s'(.*?)'", resp.text)[0]
        return sessionId
    else:
        logger.warning("sessionId获取异常!")


# 获取dinfo
def get_dinfo(sessionId):
    with open("./CryptoJs/ajk_sf.js", "r", encoding="utf-8") as f:
        js_file = f.read()
    js_obj = execjs.compile(js_file)
    dinfo = js_obj.call("AESEncrypt", taN, sessionId)
    return dinfo

def get_encryptor():
    global js_obj
    with open("./CryptoJs/ajk_sf.js", "r", encoding="utf-8") as f:
        js_file = f.read()
    js_obj = execjs.compile(js_file)
    return js_obj

# 获取responseId
def get_responseId(sessionId, dinfo):
    params["sessionId"] = sessionId
    params["dInfo"] = dinfo
    resp = requests.post(responseId_api, headers=UserAgent, params=params)
    try:
        json_data = resp.json()
        responseId = json_data["data"]["responseId"]
        return responseId
    except:
        logger.warning(f"responseId响应异常")
    
    
# 获取图片
def download_img(rid, img="_big"):
    param = {
        "rid": rid,
        "it": img,
    }

    resp = requests.get(img_api, headers=UserAgent, params=param)
    if resp.status_code == 200:
        with open(f"./imgs/{img}.jpg", "wb") as f:
            f.write(resp.content)
    else:
        logger.warning("图片下载失败")


# 获取加密轨迹
def cryped_track(track, sessionId):
    with open("./CryptoJs/ajk_sf.js", "r", encoding="utf-8") as f:
        js_file = f.read()
    js_obj = execjs.compile(js_file)
    _track = js_obj.call("AESEncrypt", track, sessionId)
    return _track


def format_track(x, track):
    _track = {"x": int(x), "track": track, "p": [0, 0]}
    return _track


def get_InfoTp(sessionId, dInfo, responsId, _data):
    data = {
        "language": "zh-CN",
    }
    data["sessionId"] = sessionId
    data["responseId"] = responsId
    data["dInfo"] = dInfo
    data["data"] = _data
    resp = requests.post(responseId_api, headers=headers, data=data)
    try:
        resp_json = resp.json()
        message = resp_json["message"]
        return message
    except:
        logger.warning(f"InfoTp响应异常")


if __name__ == "__main__":
    mylogger = MyLogger()
    logger = mylogger.logger
    total = 3
    success_count = 0
    crypto = get_encryptor()
    for i in range(total):
        sessionId = get_sessionId()
        dinfo = crypto.call("AESEncrypt", taN, sessionId)
        rid = get_responseId(sessionId, dinfo)
        download_img(rid, img="_big")
        download_img(rid, img="_puzzle")
        x = get_x()
        track_str = get_track(x)
        track = format_track(x, track_str)
        _data = crypto.call("AESEncrypt", track, sessionId)
        # _data = cryped_track(track, sessionId)
        msg = get_InfoTp(sessionId=sessionId, dInfo=dinfo, _data=_data, responsId=rid)

        if "成功" in msg:
            success_count += 1

        logger.info(f"{i+1}/{total} - x:{x} - {msg}")

    print(f"成功率:{((success_count)/total) * 100}%")
