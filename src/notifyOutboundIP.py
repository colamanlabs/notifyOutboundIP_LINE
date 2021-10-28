#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import datetime
import time
import SimpleLogger
import LineNotifyManager


def execute(file_access_token, file_ip) :
    SimpleLogger.print_msg("[execute] BEGIN")
    access_token = read_access_token(file_access_token)
    ip = read_ip(file_ip)    
    SimpleLogger.print_msg("[execute] access_token:[%s]:[%d]" % (access_token, len(access_token)))
    SimpleLogger.print_msg("[execute] ip:[%s]:[%d]" % (ip, len(ip)))    
    LineNotifyManager.sendTextMsg(access_token, ip)
    SimpleLogger.print_msg("[execute] END")


def read_access_token(file_ip) :
    SimpleLogger.print_msg("[read_access_token] BEGIN")
    SimpleLogger.print_msg("[read_access_token] file_ip:[%s]" % (file_ip))
    f = open(file_ip, 'r')    
    access_token = ''
    while True :
        line = f.readline()        
        if not line :
            break        
        #print_msg("[read_access_token] line:[%s]:[%d]" % (line, len(line)))
        access_token = line.strip()
    f.close()
    SimpleLogger.print_msg("[read_access_token] access_token:[%s]:[%d]" % (access_token, len(access_token)))
    SimpleLogger.print_msg("[read_access_token] END")
    return access_token


def read_ip(file_ip) :
    SimpleLogger.print_msg("[read_ip] BEGIN")
    SimpleLogger.print_msg("[read_ip] file_ip:[%s]" % (file_ip))
    f = open(file_ip, 'r')    
    ip = ''
    while True :
        line = f.readline()        
        if not line :
            break        
        #print_msg("[read_ip] line:[%s]:[%d]" % (line, len(line)))
        ip = line.strip()
    f.close()
    SimpleLogger.print_msg("[read_ip] ip:[%s]:[%d]" % (ip, len(ip)))
    SimpleLogger.print_msg("[read_ip] END")
    return ip


def main(file_access_token, file_ip) :        
    SimpleLogger.print_msg("[main] BEGIN")
    SimpleLogger.print_msg("[main] file_access_token:[%s]" % (file_access_token))    
    SimpleLogger.print_msg("[main] file_ip:[%s]" % (file_ip))        
    execute(file_access_token, file_ip)
    SimpleLogger.print_msg("[main] END")


if __name__ == '__main__' :
    main(sys.argv[1], sys.argv[2])
