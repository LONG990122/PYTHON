# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 15:04:28 2019

@author: Administrator
"""

import  urllib.parse
tedu = {"wd":"达内科技"}

tedu = urllib.parse.urlencode(tedu)

print (tedu)