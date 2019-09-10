# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 14:42:19 2019

@author: Administrator
"""

import urllib.request
import urllib.parse

#拼接url

baseurl = "http://www.baidu.com/s?"
key = input("请输入搜索的内容：")

#进行urlencode()编码

wd = {"wd":key}
key = urllib.parse.urlencode(wd)

url = baseurl + key

headers = {"User-Agent":"Mozilla/5.0"}
#创建请求对象

req = urllib.request.Request(url,headers = headers)

#获取响应对象

res = urllib.request.urlopen(req)
html = res.read().decode("utf-8")

#写入本地文件

with open("搜索.html","w",encoding="gb18030") as f:
    f.write(html)
