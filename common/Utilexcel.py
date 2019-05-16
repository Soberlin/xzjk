# -*- coding: utf-8 -*-
# @Time    : 2019/5/16 13:12
# @Author  : Sober
# @Site    : 
# @File    : Utilexcel.py
#pyhton  操作excel
# Header类型  数据依赖  预期结果  url  请求类型
#接口测试用例 id 模块名称 前提条件  接口地址  是否携带Header  数据依赖   请求数据  预期结果  实际结果
import xlrd   #读excel
import xlwt   #写excel
#打开excel
data=xlrd.open_workbook('../dataconfig/case1.xls')
tables=data.sheets()[0]
print(tables.nrows)
print(tables.cell_value(2,3))








