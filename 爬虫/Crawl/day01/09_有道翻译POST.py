# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 14:59:58 2019

@author: Administrator
"""
import urllib.request
import urllib.parse
import json

#请输入你要翻译的内容
key = input("请输入要翻译的内容：")
#把提交的form表单数据转为bytes数据
data = {key : key,
        "from": "AUTO",
        "to": "AUTO",
        "smartresult": "dict",
        "client": "fanyideskweb",
        "salt": "15677542532693",
        "sign": "f684d0942004bdce6d1f1f67ed377240",
        "ts": "1567754253269",
        "bv": "a4f4c82afd8bdba188e568d101be3f53",
        "doctype": "json",
        "version": "2.1",
        "keyfrom": "fanyi.web",
        "action": "FY_BY_REALTlME"
    }
#字符串  i=python&from=auto... 
data = urllib.parse.urlencode(data)
data = bytes(data,"utf-8")

#发请求
#url为POST地址
url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36"}
#此处data为form表单数据,为bytes数据类型
req = urllib.request.Request(url,data=data,headers=headers)
res = urllib.request.urlopen(req)
html = res.read().decode("utf-8")

#把json格式字符串转换为Python中字典

r_dict = json.loads(html)
print(r_dict)


#print(html)
