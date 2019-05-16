# -*- coding: utf-8 -*-
# @Time    : 2019/5/15 17:05
# @Author  : Sober
# @Site    : 
# @File    : jsontext.py
import json

# dumps是把dict转为str
# loads是把str转成dict

name_emb={'a':'1111','b':'2222','c':'3333','d':'4444'}

# jsDumps=json.dumps(name_emb)
# jsLoads=json.loads(jsDumps)
# print(name_emb)
# print(jsDumps)
# print(jsLoads)
#
# print(type(name_emb))
# print(type(jsDumps))
# print(type(jsLoads))

emb_filename=('../emb.json')
# with open(emb_filename,'w') as f:
#     f.write(jsObj)
#      f.close
# json.dump(name_emb, open(emb_filename, "w"))

jsobj=json.load(open(emb_filename))
print(jsobj)
print(type(jsobj))

# for key