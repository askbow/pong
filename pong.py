#!/usr/bin/env python

"""
    A python PONG implementation based on python-verbose_ping("script by George Notaras.
    Refer to python-ping.py for comments and authorship: http://www.g-loaded.eu/2009/10/30/python-ping/

	This file only calls python-ping functions in the same
	manner and order other PONG scripts do in their particular languages.

"""
from pythonping import * 
import csv
import time
import socket

if __name__ == '__main__':
    DataFileReader = csv.DictReader(open(r'pinglist.txt'),fieldnames=("address", "description"), delimiter=';')
    data = {}
    counter={1,2,3}
    for line in DataFileReader:
        data[line['address']]=0
        
        for i in counter:
            try:
                a = do_one(line['address'], timeout=2)#print socket.gethostbyname(line['address'])
                if a: data[line['address']] +=a
            except:
                pass
        data[line['address']]=1000*(data[line['address']]/3)
        print line['address'],"%0.4fms" % data[line['address']]
    
    #     GOOGLE
    #verbose_ping("8.8.8.8")
    while 1:
        if do_one("8.8.8.8", timeout=2): 
            print "!",
            time.sleep(1)
        else: print "."