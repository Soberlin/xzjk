# -*- coding: utf-8 -*-
# @Time    : 2019/4/30 10:21
# @Author  : Sober
# @Site    : 
# @File    : TestDemo.py
import requests
get_url = 'http://localhost:7001/XXX'
data = {'userCode':'csqy123456','userPWD':'123456'}
r = requests.get(url=get_url, params=data, timeout=5)   #产生一个名为r的Response对象,可以从这个对象中获取我们想要的信息; #get请求传参数时，使用params关键字  #timeout参数用来设定停止等待响应的时间
print(r.url)   #返回请求url
print(r.json())  #以JSON格式解析响应内容
print(r.status_code)   #返回状态码
print(r.raise_for_status())   #如果发送了一个错误请求，如404、500等，可以通过raise_for_status()来抛出异常
print(r.encoding)  #查看requests使用了什么编码，同时可以用r.encoding属性来改变它
print(r.raw)     #获取来自服务器的原始套接字响应
print(r.headers)   #服务器返回给我们的响应头信息，也可以在传参时通过headers=XXX来定制请求头
print(r.request)   #获取原来创建的Request对象
print(r.request.headers)   #发送到服务器的请求头

#封装get请求
def send_get(url,data):
    r=requests.get(url=url,params=data)
    result=r.json()
    return result

#封装post请求
def send_post(url,data):
    r=requests.get(url=url,data=data)
    result=r.json()
    return result

#定义一个主函数
def main(url,method,data):
    if method=='POST':
       r=send_post(url,data)      #如果是post请求,则调用send_post请求
    else:
       r=send_get(url,data)       #如果是get请求，则调用send_get请求
    return r

#开始调用主函数
url = 'http://localhost:7001/XXX'
data = {
    'controlSeq': '2018118325'
}
demo = main(url, 'GET', data)
print(demo)



