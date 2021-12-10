# -*- coding: gbk -*-
import re
import html
from typing import Final
from urllib import parse
import requests
import time
import pyperclip


GOOGLE_TRANSLATE_URL: Final[str] = r'http://translate.google.cn/m?q=%s&tl=%s&sl=%s'


def translate(text, to_language="auto", text_language="auto"):
    text = parse.quote(text)
    url = GOOGLE_TRANSLATE_URL % (text,to_language, text_language)
    response = requests.get(url) # TODO: if use VPN, it will not work well.
    data = response.text
    expr = r'(?s)class="(?:t0|result-container)">(.*?)<'
    result = re.findall(expr, data)
    if (len(result) == 0):
        return ""

    return html.unescape(result[0])


recent_value = ''


while True:
    tmp_value = pyperclip.paste().replace('\n', ' ').replace('\r', ' ')
    
    try:
        if tmp_value != recent_value:
            recent_value = tmp_value
            tsdata_done = translate(tmp_value, "zh-CN","en")
            print(tsdata_done)
            pyperclip.copy(tsdata_done)
        time.sleep(0.5)
    except KeyboardInterrupt:
        break
