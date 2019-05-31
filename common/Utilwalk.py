# -*- coding: utf-8 -*-
# @Time    : 2019/5/27 15:01
# @Author  : Sober
# @Site    : 
# @File    : Utilwalk.py
import os
path=r"D:\zidonghua\xzjk"
for fpath,dirname,fnames in os.walk(path):
    print(dirname)