# -*- coding: utf-8 -*-
import unittest
import ddt
from common import Config
import requests
from logs.logger import Log

test_data = [{"shareType": 1,
              "userId": 7129685,
              "title": "",
              "desc": "",
              "img_url": "http://10.0.0.32/html/index/activity?id=3295",
              "activityShare": "1"
              },
             {"shareType": 1,
              "userId": 7129685,
              "title": "行装商城",
              "desc": "行装是国内首家专注于运动，户外、旅行装备的垂直社群电商平台",
              "img_url": "http://10.0.0.32/html/index/activity?id=3295",
              "activityShare": "1"
              },
             {"shareType": 1,
              "userId": 7129685,
              "title": "行装商城",
              "desc": "行装是国内首家专注于运动，户外、旅行装备的垂直社群电商平台",
              "img_url": "http://10.0.0.32/html/index/activity?id=3295",
              "activityShare": "1"
              },
             {"shareType": 1,
              "userId": 7129685,
              "title": "行装商城",
              "desc": "行装是国内首家专注于运动，户外、旅行装备的垂直社群电商平台",
              "img_url": "http://10.0.0.32/html/index/activity?id=3295",
              "activityShare": "1"
              }
             ]
@ddt.ddt
class MyTestCase(unittest.TestCase):
    log=Log()
    @ddt.data(*test_data)
    def test_syfx(self,value):
        url = Config.MoreAdd+Config.html+Config.share
        self.log.info(url)
        reponse = requests.request("POST",url,params=value).json()
        self.log.info(reponse)
        self.assertEqual(reponse['resultCode'],2000)
        self.assertEqual(reponse['resultMsg'],'成功')
        self.assertEqual(reponse['success'],True)
        self.log.info('首页分享接口测试用例成功')
    def Add(a,b):
        return a+b


if __name__ == '__main__':
    unittest.main()
