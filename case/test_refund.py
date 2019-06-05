# -*- coding: utf-8 -*-
import unittest
from common import Config
from logs.logger import Log
from common.RunRequest import RunMain


# 订单状态
class MyTestCase(unittest.TestCase):
    log = Log();
    # 订单id
    order_id = 0;
    # 售后id
    refund_id = 0;
    #售后子id
    orId="";

    reason = {"商品污渍", "商品破损", "商品瑕疵", "商家发错货",
              "商家漏发", "商家缺货", "商家尺码不符", "发货不及时",
              "多拍/错拍", "不想要了", "未收到货", "和平台协商一致", "其他"}

    def setUp(self):
        self.log.info("测试用例方法开始")
        self.run = RunMain()

    # 测试仅退款  测试退货退款    在待发货的状态下  售后  在待收货的状态下  售后
    # 查询出待发货的订单   如果没有待发货的订单的时候 怎么处理
    # 注意点  怎么判断这个订单号有没有售后过  所以之后直接从数据库里面查询
    def test_1_Pendingorder(self):
        "查询待发货的订单"
        url = Config.MoreAdd + Config.html + Config.goodsorder
        self.log.info(url)
        data = {"userId": Config.userId, "sizePerPage": 10, "nowPageNo": 1, "orderStatus": 2,
                "pagesize": "10", "appId": Config.appId,
                "timestamp": "1550752377651", "sign": "EDFB70A66E1DADF5233551A3A0B92E11"}
        res = self.run.run_main(url, "GET", data);
        self.log.info(res)
        for x in res['data']:  # for循环拿出所有的订单号
            self.log.info(x['orderId'])
        self.log.info("========================获取第一个id")
        global order_id  # 订单号
        order_id = res['data'][0]['orderId']
        # order_id =self.log.info(res['data'][0]['orderId'])
        self.log.info("---------")
        self.log.info(order_id)
        # 断言大全
        self.assertEqual(res['resultCode'], 2000, msg="断言成功")
        self.assertEqual(res['resultMsg'], "成功", msg="断言成功")
        self.assertEqual(res['success'], True, msg="断言成功")

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
        "查询订单详情"
        url = Config.MoreAdd + Config.html + Config.goodsorderdetial
        self.log.info(url)
        self.log.info("这是第二个测试用例")
        self.log.info(order_id)  # 打印订单号
        data = {
            "userId":Config.userId,"id":order_id,"appId":Config.appId,
            "timestamp":"1550752377651","sign":"EDFB70A66E1DADF5233551A3A0B92E11"
        }
        res = self.run.run_main(url, "POST", data)
        self.log.info(res)

        # 20190408161241001
        # self.log.info("=============================================")
        # for x in res['data']['goodsOrderDetails'][0]:
        #     self.log.info(x['id'])
        # 获取达到售后id
        global refund_id;
        refund_id = res['data']['goodsOrderDetails'][0]['id']
        self.log.info(refund_id)
        self.assertEqual(res['resultCode'], 2000, msg="断言成功")
        self.assertEqual(res['resultMsg'], "成功", msg="断言成功")
        self.assertEqual(res['success'], True, msg="断言成功")

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
        "订单申请售后"
        url = Config.MoreAdd + Config.html + Config.aftermarket
        self.log.info(url)
        self.log.info("=========================这是第三个测试用例")
        self.log.info(refund_id)
        data = {
            "godId": refund_id, "appId": Config.appId,
            "timestamp": "1550752377651", "sign": "EDFB70A66E1DADF5233551A3A0B92E11"
        }
        res = self.run.run_main(url, "POST", data)
        self.log.info(res)
        self.assertEqual(res['resultCode'], 2000, msg="断言成功")
        self.assertEqual(res['resultMsg'], "成功", msg="断言成功")
        self.assertEqual(res['success'], True, msg="断言成功")

    # R201905231732407182
    # https:// m.outdoorclub.com.cn/html/aftermarket/selectAfterMarketDetailById
    # https: //m.outdoorclub.com.cn/html/aftermarke/applyAfterSale

    # {"data": {"barcode": "邮费", "createTime": 1558609451354, "gbId": 470857,
    #           "godGoodsPic": "http://res.outdoorclub.com.cn/p1/GoodsDetail/shop/2018/10/31/2529/1540966152017/1540966152017125.jpg",
    #           "goodsName": "行装商城 运动户外旅行装备 邮费补差价专用", "goodsUrl": "", "orId": "R201905231904116679", "refundAmount": 1.00,
    #           "refundNo": "R201905231904114253", "refundNum": 1, "refundReason": "商品污渍", "refundStatus": 0,
    #           "specsType": "邮费", "trackingCompany": "", "trackingNum": "", "waitTime": 1558609451354},
    #  "resultCode": 2000, "resultMsg": "成功", "success": true}
    # 申请售后   申请售后的操作
    def test_4_applyrefund(self):
        "订单售后"
        url = Config.MoreAdd + Config.html + Config.applyrefund
        self.log.info(url)
        self.log.info("===========第四个测试用例")
        data = {
            "refundUserId": Config.userId, "refundReason": "商家缺货", "refundExplain": "",
            "refundNum": 1, "refundStatus": 0, "godId": refund_id, "gbId": "470857", "gsId": "1620005", "orId": "",
            "appId": Config.appId,
            "timestamp": "1550752377651",
            "sign": "EDFB70A66E1DADF5233551A3A0B92E11"
        }
        res = self.run.run_main(url, "POST", data)
        self.log.info(res)
        global orId;
        orId = res['data']['orId']
        self.log.info(orId)
        self.log.info(res['data']['orId'])

    # http: // 10.0
        # .0
        # .35: 9080 / html / aftermarket /selectAfterMarketDetailById   返回sid  data  godId 去这个参数  post请求

     #操作步骤     sid和rid 有没有
    # http://10.0.0.32:8080/buzi/orderRefund/applyRefundOrder?id=S201905271536518423
    # 查看售后详情         orId:R201906031047482401
    def test_5_refunddetial(self):
        url = Config.MoreAdd + Config.html + Config.aftermarketById
        self.log.info("第五个测试用例=======")
        self.log.info(url)
        self.log.info(orId)
        #R  订单号
        data = {"orId":orId, "appId": Config.appId,
                       "timestamp": "1550752377651", "sign":"EDFB70A66E1DADF5233551A3A0B92E11"}
        res = self.run.run_main(url, "GET", data);
        self.log.info(res)
        self.log.info("=================")

    # id:S201906031337425032
    # statusBefore: 0
    # statusAfter: 1
    # refundId: R201906031337522688
    # message:
    # 两个提交
    # .32: 8080/buzi/orderRefund/submitRefund
    # .32: 8080/buzi/orderRefund/agreeRefund
    # 平台同意  确认
    def test_6_Agreerefund(self):
        "平台同意售后"
        url = Config.mallweb + Config.buzi+Config.mallagreerefund
        self.log.info("第6个测试用例===========")
        self.log.info(url)
        self.log.info(orId)
        data = {
            "id":refund_id,"statusBefore": 0,"statusAfter": "1","refundId":orId,"message":""
        }
        self.log.info(data)
        res = self.run.run_main(url,"GET", data)
        self.log.info(res)
    #平台确认提交售后
    def test_7_submitrefund(self):
        "平台确定售后"
        url = Config.mallweb + Config.buzi+Config.submitrefund
        self.log.info("第7个测试用例==============")
        self.log.info(url)
        self.log.info(orId)
        data = {
            "id":refund_id, "statusBefore": 1, "statusAfter": "2", "refundId":orId,
            "message": "","paramJson":{"realPayMoney":0,
                                       "realRebate": "",
                                       "realPointsRebate": "",
                                       "realOtherPointsRebate": "",
                                       "realCoin": "",
                                       "rebateSale": "",
                                       "rebateShoper": "",
                                       "rebateAgent": "",
                                       "rebatePartner": "",
                                       "refundExplain": ""
                                       }
        }
        res = self.run.run_main(url, "POST", data)
        self.log.info(res)



    # # 退货退款   退货退款密码
    # def test_receiveorder(self):
    #     url = Config.MoreAdd + Config.html + Config.aftermarket
    #     self.log.info(url)
    #     data = {
    #         "godId": 20190412162501001, "appId": Config.appId,
    #         "timestamp": "1550752377651", "sign": "EDFB70A66E1DADF5233551A3A0B92E11"
    #     }
    #     res = self.run.run_main(url, "GET", data);
    #     self.log.info(res)
    #
    # # 选取 原因售后
    # def test_receiveorder(self):
    #     url = Config.MoreAdd + Config.html + Config.aftermarket
    #     self.log.info(url)
    #     data = {
    #         "godId": 20190412162501001, "appId": Config.appId,
    #         "timestamp": "1550752377651", "sign": "EDFB70A66E1DADF5233551A3A0B92E11"
    #     }
    #     res = self.run.run_main(url, "POST", data);
    #     self.log.info(res)

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
