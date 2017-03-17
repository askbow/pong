#!/usr/bin/env python

"""
    A python PONG implementation based on python-verbose_ping("script by George Notaras.
    Refer to python-ping.py for comments and authorship: http://www.g-loaded.eu/2009/10/30/python-ping/

	This file only calls python-ping functions in the same
	manner and order other PONG scripts do in their particular languages.

"""
from pythonping import * 


if __name__ == '__main__':
    #     GOOGLE
    #verbose_ping("8.8.8.8")
    print do_one("8.8.8.8", timeout=2)