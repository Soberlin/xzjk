# -*- coding: utf-8 -*-
import unittest
from common import Config
import requests
import json
from logs.logger import Log

# 测试首页加载接口
class MyTestCase(unittest.TestCase):
    log = Log()

    def test_sy(self):
        url = Config.MoreAdd + Config.html + Config.index
        self.log.info(url)
        reponse = requests.request("Get",url).json()
        self.log.info(reponse)
        # print("resultCode:", reponse['resultCode'])
        # print("resultMsg:", reponse['resultMsg'])
        # print("success:", reponse['success'])
        self.assertEqual(reponse['resultMsg'],'成功')
        self.assertEqual(reponse['resultCode'],2000)
        self.assertEqual(reponse['success'], True)
        self.log.info("首页接口测试用例成功")

if __name__ == '__main__':
    unittest.main()
