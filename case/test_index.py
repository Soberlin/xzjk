import unittest
import requests
from common import Config
from common.GetSign import *
from common import RandomNum
from logs.logger import Log
from common.RunRequest import RunMain


class MyTestCase(unittest.TestCase):
    log = Log()

    def setUp(self):
        self.log.info('方法开始')

    # def test_index(self):
    #     url = Config.MoreAdd + Config.html + Config.index
    #     self.log.info(url)
    #     # querystring = {"timestamp":getSign13(),"sign":"BEB49195DEC0A46A7968D24A4EB5B91E", "appId":Config.appId}
    #     # self.log.info(Config.Headers)
    #     response = requests.request("GET", url, params=Config.Headers).json()
    #     self.assertEqual(response['resultCode'], 2000)
    #     self.assertEqual(response['resultMsg'], '成功')
    #     self.log.info('首页的接口测试用例结束')

    def test_search(self):
        url = Config.MoreAdd + Config.html + Config.search
        self.log.info(url)
        querystring = {"words": RandomNum.getWords(), "type": "goods_sale_count", "desc": "desc", "nowpage": "1",
                       "pagesize": "15", "userId": Config.userId, "appId": Config.appId,
                       "timestamp": "1550752377651", "sign": "EDFB70A66E1DADF5233551A3A0B92E11"}
        self.log.info(querystring)
        response = requests.request('Get', url, params=querystring).json()
        self.log.info(response)

    def test_index(self):
        url = Config.MoreAdd + Config.html + Config.index
        # self.log.info(url)
        # querystring = {"timestamp":getSign13(),"sign":"BEB49195DEC0A46A7968D24A4EB5B91E", "appId":Config.appId}
        # self.log.info(Config.Headers)
        RunMain(url,'GET',Config.Headers)
        self.log.info('首页的接口测试用例结束')

    def tearDown(self):
        self.log.info('方法结束')


if __name__ == '__main__':
    unittest.main()
