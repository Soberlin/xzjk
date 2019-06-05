# -*- coding: utf-8 -*-
# @Time    : 2019/5/22 14:22
# @Author  : Sober
# @Site    : 
# @File    : MysqlHelper.py
# python操作数据库的帮助类
import pymysql
from logs.logger import Log


class MysqlHelper:
    log = Log();

    def __init__(self, host, port, user,
                 passwd,db, charset):
        self.host = host
        self.port = port
        self.user = user
        self.passwd = passwd
        self.db = db
        self.charset = charset
        self.conn = None
        self.cur = None

    # 连接数据库
    def connectDatabase(self):
        try:
            self.conn = pymysql.connect(host=self.host, port=self.port, user=self.user, passwd=self.passwd,
                                        db=self.db, charset=self.charset)
        except:
            self.log.error("connectDatabase failed")
            return False
        self.cur = self.conn.cursor()
        return True

    # 关闭数据库
    def close(self):
        # 如果数据打开，则关闭；否则没有操作
        if self.conn and self.cur:
            self.cur.close()
            self.conn.close()
        return True

    # 执行数据库的sq语句,主要用来做插入操作
    def execute(self, sql, params=None, commit=False, ):
        # 连接数据库
        res = self.connectDatabase()
        if not res:
            return False
        try:
            if self.conn and self.cur:
                # 正常逻辑，执行sql，提交操作
                rowcount = self.cur.execute(sql, params)
                # print(rowcount)
                if commit:
                    self.conn.commit()
                else:
                    pass
        except:
            self.log.error("execute failed: " + sql)
            self.log.error("params: " + str(params))
            self.close()
            return False
        return rowcount

    # 查询所有数据
    def fetchall(self, sql, params=None):
        res = self.execute(sql, params)
        if not res:
            self.log.info("查询失败")
            return False
        self.close()
        results = self.cur.fetchall()
        self.log.info("查询成功" + str(results))
        return results

    # 查询一条数据
    def fetchone(self, sql, params=None):
        res = self.execute(sql, params)
        if not res:
            self.log.info("查询失败")
            return False
        self.close()
        result = self.cur.fetchone()
        self.log.info("查询成功" + str(result))
        return result

    # 增删改数据
    def edit(self, sql, params=None):
        res = self.execute(sql, params, True)
        if not res:
            self.log.info("操作失败")
            return False
        self.conn.commit()
        self.close()
        self.log.info("操作成功" + str(res))
        return res


if __name__ == '__main__':
    # dbManager = MysqlHelper()
    """
    sql = "select * from bandcard WHERE money>%s;"
    values = [1000]
    result = dbManager.fetchall(sql, values)
    """
    # sql = "insert into bandcard values %s,%s,%s;"
    # values = [(0, 100), (0, 200), (0, 300)]
    # result = dbManager.edit(sql, values)


    #取测试环境的测试数据
    mh = MysqlHelper('192.168.20.11',3306, 'root', 'P@ssw0rd', 'js', 'utf8')
    sql = "select * from js_userbasic where id=%s"
    sql2 = "SELECT refund_orderId FROM js_order_refund WHERE refund_status=0 and refund_userId=%s"
    result=mh.fetchone(sql,"7129685")
    result1=mh.fetchall(sql2,"7129685")
    result3=mh.fetchone(sql2,"7129685")
    print(result)
    print(result1)
    print(result3)

    # # 查询出userid为7129685的仅退款的refund_orderId
    # sql2 = 'SELECT refund_orderId FROM js_order_refund WHERE refund_status=0 and refund_userId=%s;'
    # print(mh.find(sql, '7129685'))
    # print(mh.find(sql2, '7129685'))
