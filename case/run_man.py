# -*- coding: utf-8 -*-
# @Time    : 2019/3/26 10:11
# @Author  : Sober
# @Site    : 
# @File    : run_man.py
import os
import time
import unittest
from email.mime.multipart import MIMEMultipart

from case import *
import HTMLTestRunner
import smtpd
import smtplib
from email.mime.text import MIMEText, MIMENonMultipart
from common.Config import *
from datetime import datetime, timedelta
from email import encoders
from email.header import Header
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# from config import  readCfg
# 打印当前文件夹目录

# 用例路径
# case_path = os.path.join(os.getcwd())
# print(case_path)
#
# # 报告存放路径
# report_path = os.path.join(os.getcwd(), 'report')
# print(report_path)

cur_path = os.path.dirname(os.path.realpath(__file__))
rootPath = cur_path[:cur_path.find("xzjk\\") + len("xzjk\\")]  # 获取myProject，也就是项目的根路径
print(rootPath)

# 报告存放路径
report_path = os.path.join(os.getcwd(), "report")


# 加入测试用例的方法

# def all_case():
#     discover = unittest.defaultTestLoader.discover(case_path, pattern="test*.py", top_level_dir=None)
#     print(discover)
#     return discover


def add_case(caseName="case", rule="test_*.py"):
    # 第一步，加载所有的测试用例
    case_path = os.path.join(rootPath, caseName)  # 用例文件夹
    # 如果不存在这个test文件夹,就自动创建一个
    if not os.path.exists(rootPath): os.mkdir(case_path)
    # print("case case path:%s"%case_path)
    # 定义discover方法的参数
    discover = unittest.defaultTestLoader.discover(cur_path, pattern=rule, top_level_dir=None)
    # suite=unittest.TestSuite()  #定义测试套件
    # for test_case in discover:
    #     suite.addTests(test_case)
    # print(suite)
    print(discover)
    return discover


# 生成测试报告
def run_case(all_case, reportName="report"):
    # 第二步：执行所有的测试用例，并把结果写入HTML测试报告
    now = time.strftime("%Y_%m_%d %H:%M:%S")  # 打印出当前时间
    report_path = os.path.join(rootPath, reportName)  # 测试文件夹
    print(report_path)  # 打印报告
    if not os.path.exists(report_path): os.mkdir(report_path)
    print(report_path)
    report_abspath = os.path.join(report_path, "result.html")  # 测试报告的绝对路径
    # report_path="D:\\xzjk\\report\\result.html"
    # reportPath = r'report_abspath'  # 进行转义
    # print(reportPath)
    fp = open(report_abspath, "wb")
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u'V1.0行装商城接口自动化测试用例')
    # 调用add_case函数返回值
    runner.run(all_case)
    fp.close()


# 获取测试报告
def getFile():
    path = 'D:/zidonghua/xzjk/report/'  # 设置路径
    with open(os.path.join(path, 'result.html'), 'rb') as f:
        f.read();
    return f;


def send_email(sender, sender_pass, receiver, filename):
    msg = MIMEMultipart()
    msg['From'] = sender
    msg['To'] = ','.join(receiver)
    msg['Subject'] = Header("商城系统更新回归测试", 'utf-8').encode()

    # 邮件正文是MIMEText:
    msg.attach(MIMEText('接口自动化测试V1.0测试报告,报告请查看附件', 'plain', 'utf-8'))

    # 添加附件就是加上一个MIMEBase，从本地读取一个图片:
    with open(filename, 'rb') as f:
        # 设置附件的MIME和文件名，这里是png类型:
        mime = MIMEBase('application', 'octet-stream', filename=filename)
        # 加上必要的头信息:
        mime.add_header('Content-Disposition', 'attachment', filename=filename)
        mime.add_header('Content-ID', '<0>')
        mime.add_header('X-Attachment-Id', '0')
        # 把附件的内容读进来:
        mime.set_payload(f.read())
        # 用Base64编码:
        encoders.encode_base64(mime)
        # 添加到MIMEMultipart:
        msg.attach(mime)
    smtp_server = 'smtp.exmail.qq.com'
    server = smtplib.SMTP(smtp_server, 25)  # SMTP协议默认端口是25
    server.login(sender, sender_pass)
    server.sendmail(sender, receiver, msg.as_string())
    server.quit()


# 发送测试报告到邮箱
# 1.像QQ邮箱这种ssl加密的就走SMTP_SSL，用授权码登录
# 2.其它邮箱就正常账号密码登录，走SMTP
# def send_mail(sender, psw, receiver, smtpserver, report_file, port):
#     # 发送最新的测试报告
#     with open(report_file, "rb") as f:
#         mail_body = f.read()
#     # 定义邮件内容
#     msg = MIMEMultipart()
#     body = MIMEText(mail_body, _subtype='html', _charset='utf-8')
#     msg['Subject'] = '接口自动化测试报告'
#     msg['from'] = sender
#     msg['to'] = psw
#     msg.attach(body)
#     # 添加附件
#     att = MIMEText(open(report_file, "rb").read(), "base64", "utf-8")
#     att["Content-Type"] = "application/octet-stream"
#     att["Content-Disposition"] = 'attachment;filename="report.html"'
#     msg.attach(att)
#     try:
#         smtp = smtplib.SMTP_SSL(smtpserver, port)
#     except:
#         smtp = smtplib.SMTP()
#         smtp.connect(smtpserver, port)
#     smtp.login(sender, psw)
#     smtp.sendmail(sender, receiver, msg.as_string())
#     smtp.quit()
#     print('case report email has send out')
# 运行代码
if __name__ == "__main__":
    all_case = add_case()  # 1、把所有用例加载进来
    run_case(all_case)  # 2 生成测试报告的路径
    # 邮箱配置
    # sendera = sender;
    # pswa = psw;
    # receivera = receiver;
    # smtpservera = smtp_server;
    # send_email(sender, psw, receiver,'D:/zidonghua/xzjk/report/result.html')
    # send_mail(sendera,psw,receivera, smtpserera,report_filea,porta)

