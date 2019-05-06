# -*- coding: utf-8 -*-
# @Time    : 2019/3/25 14:49
# @Author  : Sober
# @Site    : 
# @File    : GetSign.py
# 1550480146966
# 获取10位和13位的时间戳,以及时间戳转换为时间
import time, datetime
from logs.logger import Log

log=Log();

# 获取10位时间戳
def getSign10():
    t=time.time()
    print(t)
    t1=int(t)
    print(t1)
    return t1

#获取13位时间戳
def getSign13():
    t2=int(round(time.time())*1000)    #round  四舍五入了
    t2time=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(t2/1000))
    # log.info(t2)
    # log.info(t2time)
    # print(t2)
    # print(t2time)
    return t2

getSign13()


