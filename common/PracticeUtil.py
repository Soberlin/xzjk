# -*- coding: utf-8 -*-
# @Time    : 2019/5/22 19:04
# @Author  : Sober
# @Site    : 
# @File    : PracticeUtil.py

#面试题1
# 统计在一个队列中的数字，有多少个正数，多少个负数，如[1, 3, 5, 7, 0, -1, -9, -4, -5, 8]
# Python之列表生成式、生成器、可迭代对象与迭代器      https://www.cnblogs.com/yyds/p/6281453.html 网址

# [exp for iter_var in iterable if_exp]
a=[1, 3, 5, 7, 0, -1, -9, -4, -5, 8]

# 用列表生成式，生成新的列表 字符串
b=[i for  i in  a if i>0]
print("a列表大于0的个数有：%s"%len(b))

c=[i for  i in  a if i<0]
print("a列表小于0的个数有：%s"%len(c))

# 字符串 “axbyczdj”，如果得到结果“abcd”

# 字符串切片  切片方式  slice
a = "axbyczdj"
print(a[::2])

# 已知一个字符串为“hello_world_yoyo”, 如何得到一个队列 [“hello”,”world”,”yoyo”]

a = "hello_world_yoyo"
b = a.split("_")
print(b)


# 已知一个数字为1，如何输出“0001”

a = 1

print("%04d" % a)

# 已知一个队列,如： [1, 3, 5, 7], 如何把第一个数字，放到第三个位置，得到：[3, 5, 1, 7]

a = [1, 3, 5, 7]

# insert插入数据
a.insert(3, a[0])
print(a[1:])


# 已知 a = 9, b = 8,如何交换a和b的值，得到a的值为8,b的值为9


a = 8
b = 9

a, b = b, a
print(a)
print(b)

# 打印出100-999所有的”水仙花数”，所谓”水仙花数”是指一个三位数
# ，其各位数字立方和等于该数本身。例如：153是一个”水仙花数”，
# 因为153=1的三次方＋5的三次方＋3的三次方。
sxh = []
for i in range(100, 1000):
    s = 0
    m = list(str(i))
    for j in m:
        s += int(j)**len(m)
    if i == s:
        print(i)
        sxh.append(i)
print("100-999的水仙花数：%s" % sxh)

# 如果一个数恰好等于它的因子之和，则称该数为“完全数”，
# 又称完美数或完备数。 例如：第一个完全数是6，
# 它有约数1、2、3、6，除去它本身6外，其余3个数相加，
# 1+2+3=6。第二个完全数是28，
# 它有约数1、2、4、7、14、28，除去它本身28外，其余5个数相加，1+2+4+7+14=28。
# 那么问题来了，求1000以内的完全数有哪些？
a = []

for i in range(1, 1000):
    s = 0
    for j in range(1, i):
        if i % j == 0 and j < i:
            s += j
    if s == i:
        print(i)
        a.append(i)
print("1000以内完全数：%s" % a)

# 用python写个冒泡排序
a = [1, 3, 10, 9, 21, 35, 4, 6]

s = range(1, len(a))[::-1]
print(list(s))  # 交换次数

for i in s:
    for j in range(i):
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]
    print("第 %s 轮交换后数据：%s" % (len(s)-i+1, a))
print(a)


# 已知一个队列[1, 3, 6, 9, 7, 3, 4, 6]
# 已知一个队列[1, 3, 6, 9, 7, 3, 4, 6]
# 按从小到大排序
# 按从大大小排序
# 去除重复数字
a = [1, 3, 6, 9, 7, 3, 4, 6]

# 1.sort排序，正序

a.sort()
print(a)

# 2.sort倒叙

a.sort(reverse=True)
print(a)

# 3.去重

b = list(set(a))
print(b)
