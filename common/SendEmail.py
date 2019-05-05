# -*- coding: utf-8 -*-
# @Time    : 2019/3/22 12:59
# @Author  : Sober
# @Site    :
from email.header import Header
from email.mime.text import MIMEText
from email.utils import formataddr
import smtplib

# 用户信息
from_addr = 'liuguo@agleroc.com'
password = 'qiq8aC9ddhTLLnNS' #腾讯QQ邮箱或腾讯企业邮箱必须使用授权码进行第三方登陆
to_addr = ["xuhonghui@agleroc.com","liuguo@agleroc.com"]
# to_addr = 'liuguo@agleroc.com'

smtp_server = 'smtp.exmail.qq.com' # 腾讯服务器地址

# 内容初始化，定义内容格式（普通文本，html）
msg = MIMEText('测试报告', 'plain', 'utf-8')

# 发件人收件人信息格式化 ，可防空
# 固定用法不必纠结，我使用lambda表达式进行简单封装方便调用
lam_format_addr = lambda name, addr: formataddr((Header(name, 'utf-8').encode(), addr))
# 传入昵称和邮件地址
# msg['From'] = lam_format_addr('发件人昵称', from_addr) # 腾讯邮箱可略
# msg['To'] = lam_format_addr('收件人昵称（服务商会自动替换成用户名）', to_addr) # 腾讯邮箱可略


msg['From'] = from_addr # 腾讯邮箱可略
msg['To'] = to_addr # 腾讯邮箱可略

# 邮件标题
msg['Subject'] = Header('python自动化测试报告', 'utf-8').encode() # 腾讯邮箱略过会导致邮件被屏蔽

# 服务端配置，账密登陆
server = smtplib.SMTP(smtp_server, 25)

# 腾讯邮箱支持SSL(不强制)， 不支持TLS。
# server = smtplib.SMTP_SSL(smtp_server, 465) # 按需开启
# 调试模式，打印日志
# server.set_debuglevel(1) # 按需开启

# 登陆服务器
server.login(from_addr, password)

# 发送邮件及退出
server.sendmail(from_addr, [to_addr], msg.as_string()) #发送地址需与登陆的邮箱一致
server.quit()