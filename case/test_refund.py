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

    def setUp(self):
        self.log.info("测试用例方法开始")
        self.run = RunMain()

    # 测试仅退款  测试退货退款    在待发货的状态下  售后  在待收货的状态下  售后
    # 查询出待发货的订单   如果没有待发货的订单的时候 怎么处理
    def test_Pendingorder(self):
        url = Config.MoreAdd + Config.html + Config.goodsorder
        self.log.info(url)
        querystring = {"userId": Config.userId, "sizePerPage": 10, "nowPageNo": 1, "orderStatus": 2,
                       "pagesize": "10", "appId": Config.appId,
                       "timestamp": "1550752377651", "sign": "EDFB70A66E1DADF5233551A3A0B92E11"}
        res = self.run.run_main(url, "GET", querystring);
        self.log.info(res)

    # def test_orderDetail(self):
    #     id
    #     201905201809514028
    #     userId
    #     7129685
    #     timestamp
    #     1558512365845
    #     appId
    #     xingzhuang
    #     sign
    #     CE38FB7B9A62CB5507E103FB2C6C09F1


    def test_Onlyarefund(self):
        url = Config.MoreAdd + Config.html + Config.search
        self.log.info(url)
        querystring = {"words": RandomNum.getWords(), "type": "goods_sale_count", "desc": "desc", "nowpage": "1",
                       "pagesize": "10", "userId": Config.userId, "appId": Config.appId,
                       "timestamp": "1550752377651", "sign": "EDFB70A66E1DADF5233551A3A0B92E11"}
        res = self.run.run_main(url, "GET", querystring);








    def tearDown(self):
        self.log.info("测试用例结束")


    #
    # #查询待收货的订单
    # def test_receiveorder(self):
    #     url = Config.MoreAdd + Config.html + Config.search
    #     self.log.info(url)
    #     querystring = {"words": RandomNum.getWords(), "type": "goods_sale_count", "desc": "desc", "nowpage": "1",
    #                    "pagesize": "10", "userId": Config.userId, "appId": Config.appId,
    #                    "timestamp": "1550752377651", "sign": "EDFB70A66E1DADF5233551A3A0B92E11"}
    #     res = self.run.run_main(url, "GET", querystring);
    #
    #
    # #待收货状态下的退货退款
    # def test_refunds(self):
    #     url = Config.MoreAdd + Config.html + Config.search
    #     self.log.info(url)
    #     querystring = {"words": RandomNum.getWords(), "type": "goods_sale_count", "desc": "desc", "nowpage": "1",
    #                    "pagesize": "10", "userId": Config.userId, "appId": Config.appId,
    #                    "timestamp": "1550752377651", "sign": "EDFB70A66E1DADF5233551A3A0B92E11"}
    #     res = self.run.run_main(url, "GET", querystring);


if __name__ == '__main__':
    unittest.main()
