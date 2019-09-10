# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 15:19:00 2019

@author: Administrator
"""

import urllib.request
import urllib.parse
import random
import time
headers_list = [{"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36"},
                {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1"},
                {"User-Agent":"Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 2.0.50727; SLCC2; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.3; .NET4.0C; Tablet PC 2.0; .NET4.0E)"},]
headers = random.choice(headers_list)

# 主体程序
name = input("请输入贴吧名:")
begin = int(input("请输入起始页:")) 
end = int(input("请输入终止页:"))
# 对贴吧名name进行编码
kw = {"kw":name}
kw = urllib.parse.urlencode(kw)
# 拼接URL,发请求,获响应
for i in range(begin,end+1):
    # 拼接URL
    pn = (i-1)*50
    baseurl = "http://tieba.baidu.com/f?"
    url = baseurl + kw + "&pn=" + str(pn)
    # 发起请求
    req = urllib.request.Request(url,headers=headers)
    res = urllib.request.urlopen(req,timeout=5)
    time.sleep(2)
    html = res.read().decode("utf-8")
    # 写入文件
    filename = "第" + str(i) + "页.html"
    with open(filename,"w",encoding="utf-8") as f:
        print("正在爬取第%d页" % i)
        f.write(html)
        print("第%d页爬取成功" % i)
        print("*" * 30)