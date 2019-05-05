import unittest
import requests
from common import Config
from common import GetSign
from common import RandomNum
from logs.logger import Log


class MyTestCase(unittest.TestCase):
    log=Log()
    def setUp(self):
        self.log.info('开始请求，，，，，')

    def test_index(self):
        url=Config.MoreAdd+Config.html+Config.index
        self.log.info(url)
        querystring = {"timestamp":1554702176236, "sign":"BEB49195DEC0A46A7968D24A4EB5B91E", "appId":Config.appId}
        response = requests.request("GET", url, params=querystring).json()
        self.assertEqual(response['resultCode'],2000)
        self.assertEqual(response['resultMsg'],'成功')
        self.log.info('首页的接口测试用例结束')

    def test_search(self):
        url = Config.MoreAdd+Config.html+ Config.search
        self.log.info(url)
        querystring = {"words": RandomNum.getWords(), "type": "goods_sale_count", "desc": "desc", "nowpage": "1",
                       "pagesize": "15", "userId": Config.userId, "appId": Config.appId,
                       "timestamp": "1550752377651", "sign": "EDFB70A66E1DADF5233551A3A0B92E11"}
        self.log.info(querystring)
        response = requests.request('Get', url, params=querystring).json()
        self.log.info(response)

    def tearDown(self):
        self.log.info('结束了。。。。')


if __name__ == '__main__':
    unittest.main()
