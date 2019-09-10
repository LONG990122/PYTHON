# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 16:04:07 2019

@author: Administrator
"""

import re

s = """<div><p>仰天大笑出门去,我辈岂是蓬篙人</div></p>
<div><p>窗前明月光,疑是地上霜</div></p>"""
#创建编译对象，贪婪匹配
#re.S作用：使 . 能够匹配 \n 在内的所有字符
#贪婪匹配
p1 = re.compile('<div><p>.*</div></p>',re.S)
#非贪婪匹配
p2 = re.compile('<div><p>.*?</div></p>',re.S)
#匹配字符串S
r1 = p1.findall(s)

r2 = p2.findall(s)
print (r1)
print (r2)
