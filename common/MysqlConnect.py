# -*- coding: utf-8 -*-
# @Time    : 2019/4/30 11:21
# @Author  : Sober
# @Site    : 
# @File    : MysqlConnect.py
import pymysql


def get_db_conn():
    conn=pymysql.connect(
        host='host',
        user='user',
        password='password',
        port=3306,
        database='database',
        charset='utf8')
    return conn


#封装数据库查询操作
def query_db(sql):
    conn=get_db_conn()
    cur=conn.cursor()
    cur.execute(sql)
    result=cur.fetchall()
    cur.close()
    conn.close()
    return result

#封装更改数据库操作

def update_db(sql):
    conn=get_db_conn()    #获取连接
    cur=conn.cursor()    #建立游标
    try:
        cur.execute(sql)  #执行sql
        conn.commit()     #提交更改
    except Exception as e:
        conn.rollback()    #回滚
    finally:
        cur.close()   #关闭游标
        conn.close()  #关闭连接

# 封装常用数据库操作
def check_user(name):
    # 注意sql中''号嵌套的问题
    sql = "select * from user where name = '{}'".format(name)
    result = query_db(sql)
    return True if result else False


def add_user(name, password):
    sql = "insert into user (name, passwd) values ('{}','{}')".format(name, password)
    update_db(sql)

def del_user(name):
    sql = "delete from user where name='{}'".format(name)
    update_db(sql)






# from db import *

if check_user("张三"):
    del_user("张三")

