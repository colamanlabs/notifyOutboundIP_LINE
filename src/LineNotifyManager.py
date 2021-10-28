#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests
import urllib
import json
from urllib import parse
import SimpleLogger

#
# https://engineering.linecorp.com/ko/blog/using-line-notify-to-send-messages-to-line-from-the-command-line/
# https://notify-bot.line.me/my/
# https://notify-bot.line.me/doc/en/
# 
# URL 인코딩 메소드(urllib.parse.quote)
# https://docs.python.org/ko/3/library/urllib.parse.html
#
def sendTextMsg(accessToken, rawMsg) :
    SimpleLogger.print_msg("[sendTextMsg] rawMsg:[%s]" % (rawMsg))
    url = 'https://notify-api.line.me/api/notify'    
    SimpleLogger.print_msg("[sendTextMsg] url:[%s]" % (url))
    #msg = "이것은 한글테스트 123456 ABCD"   
    
    # URL 인코딩
    msg = parse.quote(rawMsg)    
    payload = 'message="' + msg + '"'
    SimpleLogger.print_msg("[sendTextMsg] payload:[%s]" % (payload))
    headers = {
        'Content-Type' : "application/x-www-form-urlencoded",
        'Cache-Control' : "no-cache",
        'Authorization' : "Bearer " + accessToken,
    }
    response = requests.request("POST", url, data=payload, headers=headers)
    responseJson = json.loads(((response.text).encode('utf-8')))
    SimpleLogger.print_msg("[sendTextMsg] responseJson:[%s]" % (responseJson))
    return responseJson 


