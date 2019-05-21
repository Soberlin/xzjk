# -*- coding: utf-8 -*-
# @Time    : 2019/5/16 20:19
# @Author  : Sober
# @Site    : 
# @File    : UtilJson.py

# class baseClass:
#     def test1(self,num):
#         print(num)
#
#
# class sonClass(baseClass):
#     def test2(self):
#         super().test1(num)
#
#
# son = sonClass()
# son.test1(11)
# 利用sum函数求和
# print(sum(range(0,101)))

# print(range(5))
#
# for i in range(5):
#     print(i)
#
#
# print(list(range(5)))
# print(list(range(0)))
#
# print(list(range(1, 0)))


# 如何在一个函数内部修改全局变量
# a=5;
#
# def fn():
#     global a
#     a=4
#
# fn()
# print(a)

# python实现列表去重的方法
# 先通过集合去重，在转列表  思路
# list=[11,11,12,13,15,15,16]
# a=set(list)
# print(a)  #
#
# print([x for x in a])
# animalslist = ['fox', 'tiger', 'rabbit', 'snake']
# for items in animalslist:
#     print(items)
#
# animalslist.append('pig')
#
# print(animalslist)
#
# del animalslist[0]
# print(animalslist)
# animalslist.sort()
# print(animalslist)
#
# for i in range(0,len(animalslist)):
#     print(animalslist[i])


#元祖
# zoo=('wolf','elephant','penguin')
# print(zoo.count('penguin'))  #统计某个元素出现的次数
# print(zoo.index('penguin'))  #统计某个元素的索引

# 记住字典中的键/值对是没有顺序的

# dict1={'zhang':'张家辉','wang':'王宝强','li':'李冰冰','zhao':'赵薇'}
# dict1['huang']='黄家驹'
# print(dict1)
# del dict1['zhao']
# print(dict1)
# #对于这种写法
# for firstname,name in dict1.items():
#     print(firstname,name)

#列表转集合 并且去重
# list1=[6,7,8,9,7,8]
# print(set(list1))
#
# #两个列表转字典
# list1 = ['key1','key2','key3']
# list2 = ['1','2','3']
#
# #嵌套列表转字典
# list3 = [['key1','value1'],['key2','value2'],['key3','value3']]
# dict(list3)
#
# print(dict(zip(list1,list2)))


# # 列表、元组转字符串
# list2 = ['a', 'a', 'b']
# print(''.join(list2))
# # 'aab'
# tup1 = ('a', 'a', 'b')
# print(''.join(tup1))
# # 'aab

# 字典转换为字符串
# dic1 = {'a':1,'b':2}
# print(str(dic1))
# "{'a': 1, 'b': 2}"

# 字典key和value互转
# dic2 = {'a': 1, 'b': 2, 'c': 3}
# {value:key for key, value in a_dict.items()}
# {1: 'a', 2: 'b', 3: 'c'}

# 字符串转列表
# s = 'aabbcc'
# list(s)
# # ['a', 'a', 'b', 'b', 'c', 'c']
#
# # 字符串转元组
# tuple(s)
# # ('a', 'a', 'b', 'b', 'c', 'c')
#
# # 字符串转集合
# set(s)
# # {'a', 'b', 'c'}
#
# # 字符串转字典
# dic2 = eval("{'name':'ljq', 'age':24}")
#
# # 切分字符串
# a = 'a b c'
# print(a.split(' '))
# # ['a', 'b', 'c']
#
# print(int(1.4))

# strip():去掉头和尾的空格
str1 = "  I love U   "
print(str1.strip())

# lstrip():去掉左侧空格
str2 = "  I love U   --"
print(str2.lstrip())

# rstrip():去掉右侧空格
str3 = "  I love U   "
print(str3.rstrip(), end='*')
print('\n')

# replace('c1','c2'),可以用replace(' ','')来去掉字符串中的所有空格
str4 = "  I love U   *"
print(str4.replace(' ', ''))


dictt={1:2,3:4,5:6,7:8}
for key, value in dictt.items():  # dictt.iteritems()
    print (key, value)
print (dictt.keys(), dictt.values())