# -*- coding: utf-8 -*-
# @Time    : 2019/3/21 10:36
# @Author  : Sober
# @Site    :
# @File    : Setting.py

#!/usr/bin/env python
#coding: utf-8
'''
unittest interface
@author: zhang_jin
@version: 1.0
@see:http://www.python-requests.org/en/master/
# import unittest
# import json
# import traceback
# import requests
# import time
# import result_statistics
# import config as cf
# from com_logger import  match_Logger
#
#
# class MyTestSuite(unittest.TestCase):
#     """docstring for MyTestSuite"""
#     #@classmethod
#     def sedUp(self):
#         print "start..."
#     #图片匹配统计
#     def test_image_match_001(self):
#         url = cf.URL1
#
#         querystring = {
#             "category": "image",
#             "offset": "0",
#             "limit": "30",
#           "sourceId": "0",
#           "metaTitle": "",
#           "metaId": "0",
#           "classify": "unclassify",
#           "startTime": "",
#           "endTime": "",
#           "createStart": "",
#           "createEnd": "",
#           "sourceType": "",
#           "isTracking": "true",
#           "metaGroup": "",
#           "companyId": "0",
#           "lastDays": "1",
#           "author": ""
#         }
#         headers = {
#             'cache-control': "no-cache",
#             'postman-token': "545a2e40-b120-2096-960c-54875be347be"
#             }
#
#
#         response = requests.request("POST", url, headers=headers, params=querystring)
#         if response.status_code == 200:
#             response.encoding = response.apparent_encoding
#             results = json.loads(response.text)
#             #预期结果与实际结果校验，调用result_statistics模块
#             result_statistics.test_result(results,196)
#         else:
#             print "http error info:%s" %response.status_code
#
#         #match_Logger.info("start image_query22222")
#         #self.assertEqual(results['total'], 888)
#
#         '''
#         try:
#             self.assertEqual(results['total'], 888)
#         except:
#             match_Logger.error(traceback.format_exc())
#         #print results['total']
#         '''
#
#     #文字匹配数据统计
#     def test_text_match_001(self):
#
#         text_url = cf.URL2
#
#         querystring = {
#             "category": "text",
#             "offset": "0",
#             "limit": "30",
#             "sourceId": "0",
#             "metaTitle": "",
#             "metaId": "0",
#             "startTime": "2017-04-14",
#             "endTime": "2017-04-15",
#             "createStart": "",
#             "createEnd": "",
#             "sourceType": "",
#             "isTracking": "true",
#             "metaGroup": "",
#             "companyId": "0",
#             "lastDays": "0",
#             "author": "",
#             "content": ""
#         }
#         headers = {
#             'cache-control': "no-cache",
#             'postman-token': "ef3c29d8-1c88-062a-76d9-f2fbebf2536c"
#             }
#
#         response = requests.request("POST", text_url, headers=headers, params=querystring)
#
#         if response.status_code == 200:
#             response.encoding = response.apparent_encoding
#             results = json.loads(response.text)
#             #预期结果与实际结果校验，调用result_statistics模块
#             result_statistics.test_result(results,190)
#         else:
#             print "http error info:%s" %response.status_code
#
#         #print(response.text)
#
#     def tearDown(self):
#         pass
#
# if __name__ == '__main__':
#     #image_match_Logger = ALogger('image_match', log_level='INFO')
#
#     #构造测试集合
#     suite=unittest.TestSuite()
#     suite.addTest(MyTestSuite("test_image_match_001"))
#     suite.addTest(MyTestSuite("test_text_match_001"))
#
#     #执行测试
#     runner = unittest.TextTestRunner()
#     runner.run(suite)
#     print "success case:",result_statistics.num_success
#     print "fail case:",result_statistics.num_fail
#     #unittest.main()
import unittest
import json
import traceback
import requests

class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.postUrl='http://10.0.0.32:9080/html/address/add.do'
        self.header={''} #根据自己实际内容填写


    def test_post01(self):
        url=self.postUrl
        header=self.header
        data={"userId":"7129685","name":"刘果","phone":"13547895623","address":"测试","isDefault":"0",
    "postCodes":"0","timestamp":"1553132084530","appId":"xingzhuang","sign":"003F7E3AACC8E24E6AC138EE5D3F6B3C"}  #根据实际内容,自己填写
        # 将data序列化为json格式数据，传递给data参数
        r=requests.post(url,data=json.dumps(data),headers=header)
        print
        r.text

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()

