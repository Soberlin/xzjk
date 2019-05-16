import unittest
import requests
from common import Config
from common.GetSign import *
from common import RandomNum
from logs.logger import Log
import json
from common.RunRequest import RunMain
from common import  Utilmock


class MyTestCase(unittest.TestCase):
    log = Log()

# @classmethod
# def setupClass(cls):
# log.info('类执行之前的方法')
# @classmethod
# def teaDownClass(cls):
# log.info('类执行之后的方法')
#注解  类方法只能执行一次

#每个用例测试之前一定要执行该方法
    def setUp(self):
        self.log.info('方法开始')
        self.run=RunMain()

    def test_index(self):
        url = Config.MoreAdd + Config.html + Config.index
        # self.log.info(url)
        # querystring = {"timestamp":getSign13(),"sign":"BEB49195DEC0A46A7968D24A4EB5B91E", "appId":Config.appId}
        # self.log.info(Config.Headers)
        res=Utilmock.mock_test(self.run.run_main,Config.Headers,url,"GET",Config.Headers)
        # res=self.run.run_main(url,'GET',Config.Headers)
        # self.assertEqual(res['resultCode'],2000,msg="断言成功")
        # self.log.info(res['resultCode'])
        self.log.info(res)
        self.log.info('首页的接口测试用例结束')

        #各种断言方法  判断两个参数是否相等  first==Second
        # self.assertEqual(self,first=,second=,msg=None)
        #判断两个参数不相等     first！=second
        # self.assertNotEqual(self, first, second, msg=None)
        #判断字符串是否包含：member in container
        # self.assertIn(self, member, container, msg=None)
        #不包含
        #self.assertNotIn(self, member, container, msg=None)
        #判断是否为真
        #self.assertTrue(self, expr, msg=None)
        #判断是否为假
        #self.assertFalse(self,expr,msg=None)
        # assertIsNone(self, obj, msg=None)
        # --判断是否为None：obj is None
        # assertIsNotNone(self, obj, msg=None)
        # --判断是否不为None：obj is not None
        # self.run.run_main()

    def tearDown(self):
        self.log.info('方法结束')


if __name__ == '__main__':
    unittest.main()
    cl
