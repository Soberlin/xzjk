# -*- coding: utf-8 -*-
# @Time    : 2019/3/25 15:59
# @Author  : Sober
# @Site    : 
# coding:utf-8
import random
import random as r

first_name = ["王", "李", "张", "刘", "赵", "蒋", "孟", "陈", "徐", "杨", "沈", "马", "高", "殷", "上官", "钟", "常"]
second_name = ["伟", "华", "建国", "洋", "刚", "万里", "爱民", "牧", "陆", "路", "昕", "鑫", "兵", "硕", "志宏", "峰", "磊", "雷", "文", "明浩",
               "光", "超", "军", "达"]
phone_start = ['134', '135', '136', '137', '138', '139', '150', '151', '152', '158', '159', '157', '182', '187', '188',
             '147', '130', '131', '132', '155', '156', '185', '186', '133', '153', '180', '189']
words=['冲锋衣','背包','凯乐石','睡袋']
#随机生成姓名
def getRandomName():
    Random=r.choice(first_name)+r.choice(second_name)
    print(Random)
    return Random
#随机生成11位数电话号码
def getRandomPhone():
    phone_e = random.randint(10000000,99999999)
    phone=r.choice(phone_start)+str(phone_e)
    print(phone)
    return phone
#随机生成搜索关键词
def getWords():
    Randomwords=random.choice(words)
    print(Randomwords)
    return Randomwords

#随机生成6位数

