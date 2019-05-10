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
SY_getNarBar=MoreAdd+getNavBar             #首页导航栏
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










