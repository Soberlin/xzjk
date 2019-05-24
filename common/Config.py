# -*- coding: utf-8 -*-
# @Time    : 2019/3/21 9:32
# @Author  : Sober
# @Site    : 
# @File    : Config.py
#代码颜色说明
#蓝色表示有文件修改没有进行提交
from common.GetSign import *

# 接口
html='/html'  #h5的接口
api='/api'    #app的接口
appId='xingzhuang'    #appId
resultCode='2000 '   #返回码
userId='7129685'     #userId

#IP+端口 生产环境
Host_name1='10.0.0.32:9080'            #线上环境商城32
Host_name2='10.0.0.35:9080'            #线上环境商城35

#测试环境
Test_name='192.168.20.2:9080'         #测试环境商城
#域名访问
MoreAdd='https://m.outdoorclub.com.cn'   #线上环境商城域名地址

MoreTestAdd='http://testm.outdoorclub.com.cn'
Pay='http://tpay.outdoorclub.com.cn'

#访问接口的头部
Headers={"timestamp":getSign13(),"sign":"BEB49195DEC0A46A7968D24A4EB5B91E","appId":appId}

#邮箱配置
sender='liuguo@agleroc.com'
psw='qiq8aC9ddhTLLnNS' #授权码
receiver=['liuguo@agleroc.com','wuxianyang@agleroc.com','mingzhenlin@agleroc.com','xuhonghui@agleroc.com','huangyan@agleroc.com','zhangxiaoke@agleroc.com','jingjing@agleroc.com']
port=25
smtp_server = 'smtp.exmail.qq.com'
#H5商城首页所有接口
getNavBar='/index/getNavBar'
SY_getNarBar=MoreAdd+getNavBar             #首页导航栏 tarBar
getNo='/sCart/getNo'
SY_getNo=MoreAdd+html+getNo             #获得卡片
notification='/notification/getUnreadCount'  #获得消息通知
SY_notification=MoreAdd+api+notification    #获取首页红点数
getQRCode='/app/getQRCode'
SY_getcode=MoreAdd+html+getQRCode      #获取个人中心二维码
index='/index/loadLayout'
SY_layout=MoreAdd+html+index       #首页接口接口资源
share='/share/lockfansurl'
SY_share=MoreAdd+share          #微信锁粉
wxConf='/wechat/getWxConf'
SY_getwx=MoreAdd+wxConf       #获得微信授权

#搜索关键词
search='/goods/selectGoodsByWords'  #搜索关键词
#商品 + 订单相关
goods='/goods/selectSkuByGoodsId'
# goodsId=12759&specId=451438&amount=1
#查询购物车
getCard='/sCart/get'
#查询品牌
goodsbrand='html/goodsbrand/query'
# http://10.0.0.35:9080/html/goodsbrand/query?originType=1
#商品详情页
goodsDetialpage='/goods/goodsDetailPage'
goodsSkuByGoodsId='/goods/selectSkuByGoodsId'
addCart='/sCart/add'

presubmit='/goodsOrder/preSubmit.do'
goodsordersubmit='/goodsOrder/updatePreSubmit.do'
goodsorder='/goodsOrder.do'
submitOrder='/commodity/submitOrder'


cancel='/orderList/orderListMain'

goodsorderdetial='/goodsOrder/goodsOrder.do'

#支付
payway='/config/get/payway'

#获取用户信息
userinfo='/easemob/getUserInfo'


#售后
aftermarket='/aftermarket/selectOrderDetailsByIds'
aftermarketById='/aftermarket/selectAfterMarketDetailById'
applyrefund='/aftermarke/applyAfterSale'



#一个下单场景 以及订单列表
#第一步        搜索--》冲锋衣--》返回整个冲锋衣数据返回一个商品list
#第二步       拿到第一个list取到商品id然后点击商品详情  返回整个商品信息   选取specid
#第三步      选取specid  加入购物车或者直接购买
#第四步      结算购物车---》申请售后---》平台自动售后成功

#查询订单列表
# 全部+待付款+待发货+待收货
# 搜索订单(商品名+订单)
# 删除订单
# 查看物流
# 确认收货




#个人中心
# 1、账户设置(个人资料、修改个人资料，账号)  收货地址(新增，编辑收货地址) 安全中心
# 2、个人中心二维码   分享二维码
# 3、可用积分（全部+收入+支出），可用装币(装币 明细 全部+收入+支出)
# 4、优惠券列表(未使用,已使用，已过期)
# 5、安全中心(设置密码)
# 6、意见反馈
# 7、签到(累计积分+签到+分享好友)
# 8、优惠券()