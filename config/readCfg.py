# -*- coding: utf-8 -*-
# @Time    : 2019/3/26 16:56
# @Author  : Sober
# @Site    : 
# @File    : readCfg.py
#专门读取配置文件的内容
import os
# import ConfigParser

cur_path=os.path.dirname(os.path.realpath(__file__))
configPath=os.path.join(cur_path,"cfg.ini")
conf=ConfigParser.ConfigParer()
conf.read(configPath)
