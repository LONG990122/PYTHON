import re
#解释： 先按照整体匹配出来，然后在匹配中()中的

#如果有2个或者多个(),则以元祖的方式取显示
s = "A B C D"

p1 = re.compile('\w+\s+\w+')

print(p1.findall(s))

p2 = re.compile('(\w+)\s+\w+')
print(p2.findall(s))

p3 = re.compile('(\w+)\s+(\w+)')
print(p3.findall(s))