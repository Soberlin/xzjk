# -*- coding: utf-8 -*-
# @Time    : 2019/5/17 13:39
# @Author  : Sober
# @Site    : 
# @File    : Utilpython.py
#补习一下python基础
# python字符串
var1='Hello World'
var2='Python Runoob'

print ("var1[0]",var1[0])
print("var2[1:5]",var2[1:5])

print("更新字符串：",var1[:6]+'Runoob')

a="Hello"
b="python"
print("a+b输出结果：",a+b)
print("a*b输出结果：",a*2)
print("a[1]输出结果：",a[1])
print("a[1:4]输出结果：",a[1:4])

if("H"in a):
    print ("H 在变量a中")
else:
    print("H 不在变量a中")

if("M" not in a):
    print("M不在变量a中")
else:
    print("M在变量a中")

print(r'\n')
print(R'\n')

print ("My name is %s and weight is %d kg!" % ('Zara', 21))

for x in [1,2,3]:
    print(x)





