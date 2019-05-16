# -*- coding: utf-8 -*-
# @Time    : 2019/5/16 12:10
# @Author  : Sober
# @Site    : 
# @File    : mock.py
import mock
#把结果模拟返回出来
#模拟mock封装
def mock_test(mock_method,request_data,url,method,response_data):
    mock_method=mock.Mock(return_value=response_data)
    res=mock_method(url,method,request_data)
    return res







