# -*- coding: utf-8 -*-
import unittest
from common import Config
from common import RandomNum
import requests
from logs.logger import Log
import json

class MyTestCase(unittest.TestCase):
    log=Log();

    def test_something(self):
        self.assertEqual(True, False)


    def test_search(self):
        url = Config.MoreAdd + Config.html + Config.search
        self.log.info(url)
        querystring = {"words":"冲锋衣", "type": "goods_sale_count", "desc": "desc", "nowpage": "1",
                   "pagesize": "15", "userId": Config.userId, "appId": Config.appId,
                   "timestamp": "1550752377651", "sign": "EDFB70A66E1DADF5233551A3A0B92E11"}
        self.log.info(querystring)
        response = requests.request('Get', url, params=querystring).json()
        data=json.loads(response)
        len=len(data)
        for i in range(0,len):
            x=data[i].get('id')
            self.log.info(x)

        self.log.info(response)


if __name__ == '__main__':
    unittest.main()
