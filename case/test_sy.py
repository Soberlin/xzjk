# -*- coding: utf-8 -*-
import unittest
from common import Config
import requests
import json
from logs.logger import Log
from common.RunRequest import RunMain

# 测试首页加载接口
class MyTestCase(unittest.TestCase):
    log = Log()
    def setUp(self):
        self.log.info('首页测试开始了。。。。')

    def test_getNarBar(self):
        self.log.info(Config.SY_getNarBar)
        RunMain(Config.SY_getNarBar,'GET',Config.Headers)
        # self.assertEqual(['resultCode'],2000)

    def test_sy(self):
        url = Config.MoreAdd + Config.html + Config.index
        self.log.info(url)
        reponse = requests.request("Get",url).json()
        self.log.info(reponse)
        self.assertEqual(reponse['resultMsg'],'成功')
        self.assertEqual(reponse['resultCode'],2000)
        self.assertEqual(reponse['success'], True)
        self.log.info("首页接口测试用例成功")

    def test_notification(self):
        self.log.info(Config.SY_notification)
        Config.Headers['userId']=7129685;
        self.log.info(Config.Headers)
        RunMain(Config.SY_notification,'GET',Config.Headers)

    def test_qrcode(self):
        self.log.info(Config.SY_getcode)
        Config.Headers['uid'] = 7129685;
        Config.Headers['type'] = 1;
        self.log.info(Config.Headers)
        RunMain(Config.SY_getcode,'GET',Config.Headers)

    def test_share(self):
        self.log.info(Config.SY_share)





    def tearDown(self):
        self.log.info('首页测试结束了。。。。')

if __name__ == '__main__':
    unittest.main()
