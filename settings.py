
sessionId_api = "https://api.anjuke.com/web/general/captchaNew.html"
responseId_api = "https://verifycode.58.com/captcha/getInfoTp"
img_api = 'https://verifycode.58.com/captcha/captcha_img'
checkinfotp_api = 'https://verifycode.58.com/captcha/checkInfoTp'

UserAgent = {
    "UserAgent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
}

taN = {
    "sdkv": "\u0033\u002e\u0030\u002e\u0031",
    "busurl": "https://api.anjuke.com/web/general/captchaNew.html",
    "useragent": UserAgent['UserAgent'],
    "clienttype": "1",
}


headers = {
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'origin': 'https://api.anjuke.com',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://api.anjuke.com/',
    'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': UserAgent['UserAgent'],
}

params = {
    "sessionId": None,
    "showType": "embed",
    "track": "",
    "clientType": "1",
    "clientId": "1",
    "language": "zh-CN",
    "dInfo": None,
}


