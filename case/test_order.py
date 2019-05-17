# -*- coding: utf-8 -*-
import unittest
from common import Config
from common import RandomNum
import requests
from logs.logger import Log
import json
from common.RunRequest import RunMain


class MyTestCase(unittest.TestCase):
    log = Log();
    # 定义一个集合
    resid = {}

    def setUp(self):
        self.log.info("测试用例方法开始")
        self.run = RunMain()

        # 搜索商品拿到商品id

    def test_search(self):
        url = Config.MoreAdd + Config.html + Config.search
        self.log.info(url)
        querystring = {"words": "冲锋衣", "type": "goods_sale_count", "desc": "desc", "nowpage": "1",
                       "pagesize": "15", "userId": Config.userId, "appId": Config.appId,
                       "timestamp": "1550752377651", "sign": "EDFB70A66E1DADF5233551A3A0B92E11"}
        res = self.run.run_main(url, "GET", querystring);
        self.log.info(res['success'])

        # 获取goodsList里面的值
        for x in res['data']['goodsList']:
            self.log.info(x['id'])
        # #获取brandList里面的值
        # for x1 in res['data']['brandList'][0]:
        # self.log.info(x1)
    #获取商品详解
    def test_goodsDetial(self):
        url=Config.MoreAdd+Config.html+Config.goodsDetialpage
        self.log.info(url)
        data = { "goodsId":55267,"userId": Config.userId, "appId": Config.appId,
                       "timestamp": "1550752377651", "sign": "EDFB70A66E1DADF5233551A3A0B92E11"}
        goodsdetail=self.run.run_main(url,"GET",data)
        self.log.info(goodsdetail)

    #获取购物车所有的sku
    def test_goodssku(self):
        url=Config.MoreAdd+Config.html+Config.goodsSkuByGoodsId
        data = {"goodsId": 55267,"appId": Config.appId,
                "timestamp": "1550752377651", "sign": "EDFB70A66E1DADF5233551A3A0B92E11"}
        goodssku = self.run.run_main(url, "GET", data)
        self.log.info(goodssku)
        for x in goodssku['data']['specMap']:
            self.log.info(x['5630;5641'])


    # def test_addgouwuche(self):





    # python 怎么对Json数组解析
    def tearDown(self):
        self.log.info("订单整体测试用例结束")


if __name__ == '__main__':
    unittest.main()
