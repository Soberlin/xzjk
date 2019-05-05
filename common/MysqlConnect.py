# -*- coding: utf-8 -*-
# @Time    : 2019/4/30 11:21
# @Author  : Sober
# @Site    : 
# @File    : MysqlConnect.py
import pymysql
class MysqlConnect(object):
      #魔术方法，初始化，构造器
      def __init__(self,host,user,password,database):
          self.db=pymysql.connect(host=host,user=user,password=password,port=3306,database=database,charset='utf8')
          self.cursor=self.db.cursor()
      #将要插入的数据写成元祖传入
      def exec_data(self,sql,data=None):
          self.cursor.execute(sql,data)
          self.db.commit()
      #sql拼接时使用repr(),将字符串原样输出
      def exce(self,sql):
          self.cursor.execute(sql)
          #提交到数据库执行
          self.db.commit()

      # def select(self,sql):






