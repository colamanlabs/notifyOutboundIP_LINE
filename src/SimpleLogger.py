# -*- coding: utf-8 -*-
 
import datetime
import time


def print_msg(str_msg) :
    timestamp = time.strftime('%Y%m%d_%H%M%S', time.localtime())
    #print(type(timestamp))
    msg = "[%s] %s" % (timestamp, str_msg)
    print(msg)
    