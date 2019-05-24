# -*- coding: utf-8 -*-
import unittest
from common import Config
from logs.logger import Log
from common.RunRequest import RunMain


# 订单状态
class MyTestCase(unittest.TestCase):
    log = Log();
    order_id = 0;

    def setUp(self):
        self.log.info("测试用例方法开始")
        self.run = RunMain()

    # 测试仅退款  测试退货退款    在待发货的状态下  售后  在待收货的状态下  售后
    # 查询出待发货的订单   如果没有待发货的订单的时候 怎么处理
    #注意点  怎么判断这个订单号有没有售后过  所以之后直接从数据库里面查询
    def test_1_Pendingorder(self):
        url = Config.MoreAdd + Config.html + Config.goodsorder
        self.log.info(url)
        data = {"userId": Config.userId, "sizePerPage": 10, "nowPageNo": 1, "orderStatus": 2,
                "pagesize": "10", "appId": Config.appId,
                "timestamp": "1550752377651", "sign": "EDFB70A66E1DADF5233551A3A0B92E11"}
        res = self.run.run_main(url, "GET", data);
        self.log.info(res)                  #可以拿出所有的订单号
        for x in res['data']:
            self.log.info(x['orderId'])
        # self.assertEqual(goodsadd['resultCode'], 2000, msg="断言成功")
        self.assertEqual(res['resultCode'],2000,msg="断言成功")
        self.assertEqual(res['resultMsg'],"成功",msg="断言成功")
        self.assertEqual(res['success'],True,msg="断言成功")

    # #查询出待收货的订单
    # def test_receivedorder(self):
    #     url = Config.MoreAdd + Config.html + Config.goodsorder
    #     self.log.info(url)
    #     querystring = {"userId": Config.userId, "sizePerPage": 10, "nowPageNo": 1, "orderStatus": 3,
    #                    "pagesize": "10", "appId": Config.appId,
    #                    "timestamp": "1550752377651", "sign": "EDFB70A66E1DADF5233551A3A0B92E11"}
    #     res = self.run.run_main(url, "GET", querystring);
    #     self.log.info(res)
    # 获取订单详情    201007664203952128
    def test_2_goodsorderdetail(self):
        url = Config.MoreAdd + Config.html + Config.goodsorderdetial
        self.log.info(url)
        data = {
                "userId": Config.userId, "id": 214360365063073792, "appId": Config.appId,
                "timestamp": "1550752377651", "sign": "EDFB70A66E1DADF5233551A3A0B92E11"
        }
        res = self.run.run_main(url, "POST", data)
        self.log.info(res)
        self.assertEqual(res['resultCode'], 2000, msg="断言成功")
        self.assertEqual(res['resultMsg'], "成功", msg="断言成功")
        self.assertEqual(res['success'], True, msg="断言成功")
        # 20190408161241001
        self.log.info("=============================================")
        # for x in res['data']['goodsOrderDetails'][0]:
        #     self.log.info(x['id'])
        #获取达到售后id
        self.log.info(res['data']['goodsOrderDetails'][0]['id'])



    # 获取用户信息     214360365063073792
    # def test_3_userInfo(self):
    #     url=Config.MoreAdd+Config.html+Config.userinfo
    #     self.log.info(url)
    #     data={
    #         "userId": Config.userId, "userName":"hx_name7129685",
    #         "timestamp": "1550752377651", "sign": "EDFB70A66E1DADF5233551A3A0B92E11"
    #     }
    #     res=self.run.run_main(url,"GET",data)
    #     self.log.info(res)

    # 申请售后
    # https://m.outdoorclub.com.cn/html/aftermarket/selectOrderDetailsByIds
    def test_3_aftermarket(self):
        url = Config.MoreAdd + Config.html + Config.aftermarket
        self.log.info(url)
        data = {
            "godId": 20190408161241001, "appId": Config.appId,
            "timestamp": "1550752377651", "sign": "EDFB70A66E1DADF5233551A3A0B92E11"
        }
        res = self.run.run_main(url, "POST", data)
        self.log.info(res)
    # R201905231732407182
    # https:// m.outdoorclub.com.cn/html/aftermarket/selectAfterMarketDetailById
    # https: //m.outdoorclub.com.cn/html/aftermarke/applyAfterSale

    # {"data": {"barcode": "邮费", "createTime": 1558609451354, "gbId": 470857,
    #           "godGoodsPic": "http://res.outdoorclub.com.cn/p1/GoodsDetail/shop/2018/10/31/2529/1540966152017/1540966152017125.jpg",
    #           "goodsName": "行装商城 运动户外旅行装备 邮费补差价专用", "goodsUrl": "", "orId": "R201905231904116679", "refundAmount": 1.00,
    #           "refundNo": "R201905231904114253", "refundNum": 1, "refundReason": "商品污渍", "refundStatus": 0,
    #           "specsType": "邮费", "trackingCompany": "", "trackingNum": "", "waitTime": 1558609451354},
    #  "resultCode": 2000, "resultMsg": "成功", "success": true}
    #申请售后   申请售后的操作
    def test_4_applyrefund(self):
        url=Config.MoreAdd+Config.html+Config.applyrefund
        self.log.info(url)
        data = {
            "refundUserId": 20190408161241001,"refundReason":"桑普问题","refundReason":"1",
            "appId": Config.appId,"refundReason":"refundReason","refundReason":"refundReason",
            "timestamp": "1550752377651", "sign": "EDFB70A66E1DADF5233551A3A0B92E11"
        }
        res = self.run.run_main(url, "POST", data)
        self.log.info(res)


    #查看售后详情
    def test_5_Onlyarefund(self):
        url = Config.MoreAdd + Config.html + Config.aftermarketById
        self.log.info(url)
        data = {"orId":"R201905231732407182", "appId": Config.appId,
                       "timestamp": "1550752377651", "sign": "EDFB70A66E1DADF5233551A3A0B92E11"}
        res = self.run.run_main(url, "GET", data);
        self.log.info(res)




    # 退货退款   退货退款密码
    def test_receiveorder(self):
        url = Config.MoreAdd + Config.html + Config.aftermarket
        self.log.info(url)
        data = {
            "godId": 20190412162501001, "appId": Config.appId,
            "timestamp": "1550752377651", "sign": "EDFB70A66E1DADF5233551A3A0B92E11"
        }
        res = self.run.run_main(url, "GET", data);
        self.log.info(res)

    # 选取 原因售后
    def test_receiveorder(self):
        url = Config.MoreAdd + Config.html + Config.aftermarket
        self.log.info(url)
        data = {
            "godId": 20190412162501001, "appId": Config.appId,
            "timestamp": "1550752377651", "sign": "EDFB70A66E1DADF5233551A3A0B92E11"
        }
        res = self.run.run_main(url, "POST", data);
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



    def tearDown(self):
        self.log.info("测试用例结束")

    #
    # #查询待收货的订单

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
