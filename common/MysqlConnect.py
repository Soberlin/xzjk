# -*- coding: utf-8 -*-
# @Time    : 2019/4/30 11:21
# @Author  : Sober
# @Site    : 
# @File    : MysqlConnect.py
import pymysql


# def get_db_conn():
#     conn=pymysql.connect(
#         host='ip',
#         user='user',
#         password='password',
#         port=3306,
#         database='database',
#         charset='utf8')     #创建连接
#     return conn


# #封装数据库查询操作
# def query_db(sql):
#     conn=get_db_conn()
#     cur=conn.cursor()
#     cur.execute(sql)
#     result=cur.fetchall()
#     cur.close()
#     conn.close()
#     return result


# #封装更改数据库操作
#
# def update_db(sql):
#     conn=get_db_conn()    #获取连接
#     cur=conn.cursor()    #建立游标
#     try:
#         cur.execute(sql)  #执行sql
#         conn.commit()     #提交更改
#     except Exception as e:
#         conn.rollback()    #回滚
#     finally:
#         cur.close()   #关闭游标
#         conn.close()  #关闭连接


# # 封装常用数据库操作
# def check_user(name):
#     # 注意sql中''号嵌套的问题
#     sql = "select * from user where name = '{}'".format(name)
#     result = query_db(sql)
#     return True if result else False
#
#
# def add_user(name, password):
#     sql = "insert into user (name, passwd) values ('{}','{}')".format(name, password)
#     update_db(sql)
#
# def del_user(name):
#     sql = "delete from user where name='{}'".format(name)
#     update_db(sql)



# # from db import *
#
# if check_user("张三"):
#     del_user("张三")

# conn = pymysql.connect(host="192.168.20.11",user='root',password='P@ssw0rd',database="js")
# cursor=conn.cursor()
# sql="SELECT * FROM js_userbasic WHERE id=7129685"
# #执行sql
# cursor.execute(sql)
# #返回查询结果
# result=cursor.fetchone()
# cursor.close()
# conn.close()
# print(result)


#查询订单

from common.MysqlHelper import MysqlHelper

mh = MysqlHelper('192.168.20.11', 3306,'root', 'P@ssw0rd', 'js', 'utf8')
sql = "select * from js_userbasic where id=%s"

# 查询出userid为7129685的仅退款的refund_orderId
sql2='SELECT refund_orderId FROM js_order_refund WHERE refund_status=0 and refund_userId=%s;'
print(mh.find(sql, '7129685'))
print(mh.find(sql2, '7129685'))
# sql2 = "insert into js_userbasic(name,password) values(%s,%s)"
# mh.cud(sql2, ('小光', '123456'))


