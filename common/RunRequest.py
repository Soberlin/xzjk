# -*- coding: utf-8 -*-
# @Time    : 2019/4/30 10:36
# @Author  : Sober
# @Site    : 
# @File    : RunMadin.py
import requests
import json
from logs.logger import Log
from common import RandomNum
from common import Config
from logs.logger import Log
class RunMain:
    log=Log();
    # """含有构造器"""
    # def __init__(self,url,method,data=None):
    #     self.t=self.run_main(url,method,data)

    def send_post(self,url,data):
        try:
            r=requests.post(url=url,data=data)
            result=r.json()
            self.log.info("post请求的响应内容：%s"%result)
            self.log.info("post请求返回的状态码：%s"%r.status_code)
            self.log.info("post接口响应时间：%s"%r.elapsed.total_seconds())
            return result
            # return json.dumps(result,indent=2,sort_keys=True,ensure_ascii=False)
        except Exception as e:
            self.log.info("post请求错误：%e"%e)
    #利用json，dumps将响应数据进行json格式的编码解析
    #indent=2将输出结果缩进2个字符显示
    #sort_keys=False,输出结果是否按照关键字排序
    #json。dumps 序列化时对中文默认使用的ASCII编码 ensure_ascii 才会输出中文
    #return  result
    def send_get(self,url,data):
        try:
            r=requests.get(url=url,params=data)
            result=r.json()
            self.log.info("get请求的响应内容：%s"%result)
            # self.log.info("get请求返回的状态码：%s"%r)
            self.log.info("get请求的url:%s"%url)
            self.log.info("get接口响应时间：%s" % r.elapsed.total_seconds())
            return result
            # return  json.dumps(result,indent=2,sort_keys=True,ensure_ascii=False)
        except Exception as e:
            self.log.info("get请求错误：%e"%e)

    #main方法
    def run_main(self,url,method,data=None):
        if method=='GET':
           r=self.send_get(url,data)
        else:
           r=self.send_post(url,data)
        return r

# if __name__=='__main__':
#     url= Config.MoreAdd + Config.html + Config.search
#     querystring = {"words": RandomNum.getWords(), "type": "goods_sale_count", "desc": "desc", "nowpage": "1",
#                        "pagesize": "15", "userId": Config.userId, "appId": Config.appId,
#                        "timestamp": "1550752377651", "sign": "EDFB70A66E1DADF5233551A3A0B92E11"}
#
#     test = RunMain(url,'GET',querystring)  # 因为有构造器 __init__，实例化时要带参数
#     print(test)
