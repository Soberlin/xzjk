# -*- coding: utf-8 -*-
# @Time    : 2019/5/23 19:40
# @Author  : Sober
# @Site    : 
# @File    : RedisHelper.py
#python操作Redis   python操作redis
import redis
# r=redis.Redis(host='192.168.20.10',port=6389,password='redisredis')  #主机 端口  db
# # r.set()                                                            #添加
# r.set('name', 'root')
# print(r.get('name').decode('utf8'))
# # print(r(type))




pool = redis.ConnectionPool(host='192.168.20.10',password='redisredis')   #实现一个连接池
r = redis.Redis(connection_pool=pool)
r.set('foo','bar')
print(r.get('foo').decode('utf8'))