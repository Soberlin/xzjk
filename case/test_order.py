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
    # 定义一个全局变量
    # 商品di
    Goods_id = 0;
    # skuid
    Sku_id = 0;
    #id
    Order_id=0;

    # 最新应该是清空购物车

    def setUp(self):
        self.log.info("测试用例方法开始")
        self.run = RunMain()

        # 搜索商品拿到商品id

    def test_1_search(self):
        url = Config.MoreAdd + Config.html + Config.search
        self.log.info(url)
        querystring = {"words": RandomNum.getWords(), "type": "goods_sale_count", "desc": "desc", "nowpage": "1",
                       "pagesize": "10", "userId": Config.userId, "appId": Config.appId,
                       "timestamp": "1550752377651", "sign": "EDFB70A66E1DADF5233551A3A0B92E11"}
        res = self.run.run_main(url, "GET", querystring);
        self.log.info(res['success'])
        global Goods_id

        Goods_id = res['data']['goodsList'][0]['id']
        self.log.info(Goods_id)
        # 获取goodsList里面的值
        # for x in res['data']['goodsList'][0]:
        #     # self.log.info(type(x))
        #     self.log.info(x['id'])
        # #获取brandList里面的值
        # for x1 in res['data']['brandList'][0]:
        # self.log.info(x1)

    # 获取商品详解
    def test_2_goodsDetial(self):
        url = Config.MoreAdd + Config.html + Config.goodsDetialpage
        self.log.info(url)
        data = {"goodsId": Goods_id, "userId": Config.userId, "appId": Config.appId,
                "timestamp": "1550752377651", "sign": "EDFB70A66E1DADF5233551A3A0B92E11"}
        self.log.info(data)
        goodsdetail = self.run.run_main(url, "GET", data)
        self.log.info(goodsdetail)

    # 获取商品所有的sku
    def test_3_goodssku(self):
        url = Config.MoreAdd + Config.html + Config.goodsSkuByGoodsId
        data = {"goodsId": Goods_id, "appId": Config.appId,
                "timestamp": "1550752377651", "sign": "EDFB70A66E1DADF5233551A3A0B92E11"}
        goodssku = self.run.run_main(url, "GET", data)
        self.log.info(goodssku)
        res = goodssku['data']['specMap']
        self.log.info('====================================')
        self.log.info(res)

        listt = []

        for x in res.values():
            listt.append(x['gmSpeId'])
        self.log.info(listt)

        global Sku_id
        self.log.info(listt[0])
        Sku_id = listt[0]

        # dictt = {}
        # for key,value in res.items():
        #     dictt[key] = value
        # self.log.info(dictt)
        # self.log.info(dictt.values('gmSpeId'))
        # self.log.info(type(dictt))
        # self.log.info(dictt[0])
        # self.log.info(dictt['5631;5645'])
        # for x in goodssku['data']['specMap']['5631;5642']:
        # self.log.info(x['id'])

    # 加入购物车      amount 参数如果是1的话后续要考虑太多
    # def test_4_addgouwuche(self):
    #     url = Config.MoreAdd + Config.html + Config.addCart
    #     self.log.info(url)
    #     data = {
    #         "userId": Config.userId, "goodsId": Goods_id, "appId": Config.appId, "specId": Sku_id, "amount": 1,
    #         "timestamp": "1550752377651", "sign": "EDFB70A66E1DADF5233551A3A0B92E11"
    #     }
    #     goodsadd = self.run.run_main(url, "GET",data)
    #     self.log.info(goodsadd)
    #     self.assertEqual(goodsadd['resultCode'], 2000, msg="断言成功")
    #     self.assertEqual(goodsadd['resultMsg'], "成功", msg="断言成功")
    #     self.log.info(Sku_id)

    # 清理购物车逻辑

    #提交预订单      buyMode 0
    def test_5_presubmit(self):
        url = Config.MoreAdd + Config.html + Config.presubmit
        self.log.info(url)
        data = {
            "userId": Config.userId, "goodsOrderDetailsJson": [{"specsId": Sku_id, "number": 1}], "appId": Config.appId,"buyMode":0,
            "timestamp": "1550752377651", "sign": "EDFB70A66E1DADF5233551A3A0B92E11"
        }
        presubmit = self.run.run_main(url, "POST", data)
        self.log.info(presubmit)
        self.log.info(presubmit['data']['id'])

        # 订单号
        global Order_id
        Order_id=self.log.info(presubmit['data']['id'])

    #提交预订单
    def test_6_submitOrder(self):
        url = Config.MoreAdd + Config.html + Config.submitOrder
        self.log.info(url)
        data = {
            "advanceOrderId": Order_id,
        }
        submitOrder = self.run.run_main(url, "GET", data)
        self.log.info(submitOrder)

    #再次提交预订单
    def test_7_submitOrder(self):
        url = Config.MoreAdd + Config.html + Config.submitOrder
        self.log.info(url)
        data = {
            "advanceOrderId": Order_id, "userToken": Config.userId
        }
        submitOrder = self.run.run_main(url, "GET", data)
        self.log.info(submitOrder)

    #提交订单
    def test_8_goodsorder(self):
        url = Config.MoreAdd + Config.html + Config.goodsorder
        self.log.info(url)
        data = {"userId": Config.userId, "id": Order_id, "shippingMode": 1, "appId": Config.appId,
                "timestamp": "1550752377651", "sign": "EDFB70A66E1DADF5233551A3A0B92E11"}
        orderdo = self.run.run_main(url, "POST", data)
        self.log.info(orderdo)

    # #取消订单
    def test_9_cancelorder(self):
        url=Config.MoreAdd+Config.html+Config.cancel
        self.log.info(url)
        data = {"choose":1}
        cancelorder = self.run.run_main(url,"GET",data)
        self.log.info(cancelorder)

    #再次取消订单
    # def test_10_cancelorderdo(self):
    #     url=Config.MoreAdd+Config.html+Config.cancel
    #     self.log.info(url)
    #     data = {"choose":1,"userToken":"CEFMBLA"}
    #     cancelorder = self.run.run_main(url,"GET",data)
    #     self.log.info(cancelorder)





# #  判断支付开关
# def test_5_pay(self):
#     url = Config.Pay + Config.payway
#     self.log.info(url)
#     data = {"userId": 7129685, "timestamp": "1550752377651"}
#     #返回支付参数
#     # {"HXAPPLETS": "1", "HXH5": 1, "HXQUICK": "1", "HXAPP": "1"}
#     paydata = self.run.run_main(url, "POST", data)
#     self.log.info(paydata)
#
#
#
# #用户提交订单 id是动态参数
# def test_6_ordersumbit(self):
#     url=Config.MoreAdd+Config.html+Config.goodsordersubmit
#     self.log.info(url)
#     data={"userId": 7129685, "id": 201905201015184026, "appId": Config.appId,
#         "timestamp": "1550752377651", "sign": "EDFB70A66E1DADF5233551A3A0B92E11"}
#     ordersubmit = self.run.run_main(url, "POST", data)
#     self.log.info(ordersubmit)
#
#
#
# #支付订单 id是动态参数

# python 怎么对Json数组解析


def tearDown(self):
    self.log.info("订单整体测试用例结束")


if __name__ == '__main__':
    unittest.main()
