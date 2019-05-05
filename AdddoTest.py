# -*- coding: utf-8 -*-
# @Time    : 2019/3/21 9:35
# @Author  : Sober
# @Site    : 
# @File    : AdddoTest.py
import  requests
import unittest
import json
import traceback

url="http://10.0.0.32:9080/html/address/add.do"

# userId: 7129685
# name: 刘果
# phone: 13547895623
# area: 辽宁省 大连市 中山区
# address: 测试
# isDefault: 0
# postCodes:
# timestamp: 1553132084530
# appId: xingzhuang
# sign: 003F7E3AACC8E24E6AC138EE5D3F6B3C

querything={
    "userId":"7129685","name":"刘果","phone":"13547895623","address":"测试","isDefault":"0",
    "postCodes":"0","timestamp":"1553132084530","appId":"xingzhuang","sign":"003F7E3AACC8E24E6AC138EE5D3F6B3C"
}
header={'content-type':'application/x-www-form-urlencoded; charset=UTF-8'}


try:
    #Post接口调用
    response = requests.request("POST", url, headers=header, params=querything)

    #对http返回值进行判断，对于200做基本校验
    if response.status_code == 200:
        results = json.loads(response.text)
        if results['total'] == 191:
            print
            "Success"
        else:
            print
            "Fail"
            print
            results['total']
    else:
        #对于http返回非200的code，输出相应的code
        raise Exception("http error info:%s" %response.status_code)
except:
    traceback.print_exc()


print(response.text)


#对返回结果进行转义成json串
results=json.loads(response.text)

#获取http请求的status_code
print="Http code:",response.status_code

print=results['total']

# 接口调用异常处理，
# 增加try，except处理，
# 对于返回response.status_code，
# 返回200进行结果比对，不是200数据异常信息。






