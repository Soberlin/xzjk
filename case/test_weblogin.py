# -*- coding: utf-8 -*-
import unittest
from common import Config
from logs.logger import Log
from common.RunRequest import RunMain
import sys
import io
import requests


class MyTestCase(unittest.TestCase):
    log = Log()

    def setUp(self):
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='gb18030')
        self.log.info("测试用例方法开始")
        self.run = RunMain()

    def test_checkcode(self):
        url = 'http://10.0.0.32:8080/PictureCheckCode.jpeg'
        res = self.run.run_main(url, "GET")
        self.log.info(res)

    def test_login(self):
        url = "http://10.0.0.32:8080/loginsubmit"
        data = {"loginName": "outfit-liuguo",
                "password": "liuguo123"
                }  # get方法其它加个ser-Agent就可以了
        res = self.run.run_main(url, "POST", data)
        self.log.info(res)

    def test_6_Agreerefund(self):
        "平台同意售后"
        url = Config.testmallweb + Config.buzi+Config.mallagreerefund
        self.log.info("第6个测试用例===========")
        self.log.info(url)
        data = {
            "id":"S201906041642560508","statusBefore": 0,"statusAfter": "1","refundId":"R201905201513473203","message":""}
        self.log.info(data)
        res = self.run.run_main(url,"GET", data)
        self.log.info(res)


    def tearDown(self):
        self.log.info("测试用例结束")

    if __name__ == '__main__':
        unittest.main()
