#!/bin/python
# -*- coding: utf-8 -*-
from __future__ import print_function
from __future__ import unicode_literals
from __future__ import division
from __future__ import absolute_import
try:
    from future_builtins import *
except ImportError:
    pass


"""
    A python PONG implementation based on python-verbose_ping("script by George Notaras.
    Refer to python-ping.py for comments and authorship: http://www.g-loaded.eu/2009/10/30/python-ping/

    This file only calls python-ping functions in the same
    manner and order other PONG scripts do in their particular languages.
	
	Now includes HTTP-ping capability 
    # AWS targets and HTTP ping idea credit http://www.cloudping.info/
"""
from pythonping import * 
import csv
import time
import socket
import os
import sys
import requests
import string
import random

def ___HTTPCall___(URI="", HTTP_TIMEOUT = 1):
    #
    if URI == "" : return None
    URI = URI +  "ping?x=" + ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(8))
    if HTTP_TIMEOUT < 1: HTTP_TIMEOUT = 1
    start = time.time()
    try:
        r = requests.get(URI, timeout=HTTP_TIMEOUT)
    except: raise  
    roundtrip = time.time() - start
    return roundtrip

def main():
    with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), r'pinglist.txt')) as f:
        data = {}
        counter={1,2,3}
        for line in csv.DictReader(f,fieldnames=("address", "description"), delimiter=';'):
            data[line['address']]=0
            
            for i in counter:
                try:
                    a = do_one(line['address'], timeout=2)#print socket.gethostbyname(line['address'])
                    if a: data[line['address']] +=a
                except:
                    pass
            data[line['address']]=1000*(data[line['address']]/3)
            print(line['description'], line['address'],"%0.4fms" % data[line['address']] )
    with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), r'httppinglist.txt')) as f:
        data = {}
        counter = {1,2,3}
        for line in csv.DictReader(f,fieldnames=("endpoint", "name"), delimiter=';'):
            data[line['endpoint']] = 0
            for i in counter:
                try:
                    a = ___HTTPCall___(line["endpoint"])
                    if a: data[line['endpoint']] += a
                except:
                    pass
            data[line['endpoint']]=1000*(data[line['endpoint']]/3)
            print(line["name"],"%0.4fms" % data[line['endpoint']]  )
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
if __name__ == '__main__':        
    main()