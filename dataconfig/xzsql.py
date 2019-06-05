# -*- coding: utf-8 -*-
# @Time    : 2019/6/4 17:47
# @Author  : Sober
# @Site    : 
# @File    : xzsql.py
#查询退货退款的数据   仅退款
onlyrefund="SELECT refund_orderId FROM js_order_refund WHERE refund_status=0 and refund_userId=7129685"
