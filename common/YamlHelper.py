# -*- coding: utf-8 -*-
# @Time    : 2019/5/22 11:10
# @Author  : Sober
# @Site    : 
# @File    : Utilyaml.py
import yaml
import os
from ruamel import yaml

desired_caps = {
    'platformName': 'Android',
    'platformVersion': '7.0',
    'deviceName': 'A5RNW18316011440',
    'appPackage': 'com.tencent.mm',
    'appActivity': '.ui.LauncherUI',
    'automationName': 'Uiautomator2',
    'unicodeKeyboard': [True, "hh"],
    'resetKeyboard': True,
    'noReset': True,
    'chromeOptions': {'androidProcess': 'com.tencent.mm:tools'}
}
curpath = os.path.dirname(os.path.realpath(__file__))
print(curpath)
yamlpath = os.path.join(curpath, "Cfg.yaml")
print(yamlpath)

#写入到yaml文件
with open(yamlpath, "w", encoding="utf-8") as f:
    yaml.dump(desired_caps,f,Dumper=yaml.RoundTripDumper)

#读文件
a=open(yamlpath,"r")
print(yaml.load(a.read(),Loader=yaml.Loader))


def read_yaml(self,path):
    result=open(path,"r")
    print(yaml.load(result.read()))
    return yaml.load(result.read())