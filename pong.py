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
# pong.py
# Tests Internet connectivity
# 
# MIT license
# (c) Denis Borchev 
    
    Refer to python-ping.py for comments and authorship: http://www.g-loaded.eu/2009/10/30/python-ping/

    Includes HTTP-ping capability 
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
from math import inf
from multiprocessing import Pool

# As per http://comparch.gatech.edu/hparch/gupta_tr12.pdf
# Plus my educated guess is, optimal performance is achieved (for most practical cases)
# at around 8-16; consider how many cores / threads you have in your system as the upper limit on this
SETTING_PROCESSES = 8
SETTING_TIMEOUT = 2

def ___HTTPCall___(URI=""):
    #if URI=="" : return inf
    URI = URI +  "ping?x=" + ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(8))
    roundtrip = inf
    try:
        start = time.time()
        r = requests.get(URI, timeout=SETTING_TIMEOUT)
        roundtrip = time.time() - start
    except: pass  
    return roundtrip

def ___ICMPecho___(host=None):
    roundtrip = inf
    if host==None: return inf
    try:
        roundtrip = do_one(host, timeout=SETTING_TIMEOUT)#print socket.gethostbyname(line['address'])
    except: pass  
    return roundtrip
    
def __pong__(target=dict()):    
    result = dict()
    result['name'] = target['name']
    roundtrip = inf
    if target['type'] == 'http':      roundtrip = ___HTTPCall___(URI = target["endpoint"] )
    if target['type'] == 'icmp-echo': roundtrip = ___ICMPecho___(target["endpoint"] )
    result['roundtrip'] = roundtrip
    return result
    
def load():
    data = list()
    with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), r'pinglist.txt')) as f:
        for line in csv.DictReader(f,fieldnames=("address", "description"), delimiter=';'):
            d=dict()
            d['type'] = 'icmp-echo'
            d["endpoint"] = line["address"]
            d["name"] = line["description"]
            data.append(d)
    #
    with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), r'httppinglist.txt')) as f:
        for line in csv.DictReader(f,fieldnames=("address", "description"), delimiter=';'):
            d=dict()
            d['type'] = 'http'
            d["endpoint"] = line["address"]
            d["name"] = line["description"]
            data.append(d)
    return data
        
def main():
    a = list()
    TARGETS = load()
    with Pool(SETTING_PROCESSES) as p:
	    a = p.map( __pong__ , TARGETS) 
    for l in a:
        print(l['name'],l['roundtrip'])
        
if __name__ == '__main__':        
    main()