# -*- coding: utf-8 -*-
# @Time    : 2019/3/21 10:54
# @Author  : Sober
# @Site    : 
# @File    : logger.py
import logging

logging.info("this is info")
Log_FileName='/root/common/log.txt'
logging.basicConfig(filename=Log_FileName,level=logging.INFO)
logging.info("This message should go to the file")