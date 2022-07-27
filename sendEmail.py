#!/usr/bin/python
# -*- coding: UTF-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.header import Header

def send_email(content):
    KEY = 'dwioiqbbtzgsdbgge'
    EMAIL_ADDRESS = '474754765@qq.com'  # 换成你的邮箱地址
    sender = EMAIL_ADDRESS
    receivers = ['wangjitao2@outlook.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

    # 三个参数：第一个为文本内容，第二个 plain 设置文本格式，第三个 utf-8 设置编码
    message = MIMEText(content, 'plain', 'utf-8')
    message['From'] = 'jt <474754765@qq.com>'   # 发送者
    message['To'] = ';'.join(receivers)        # 接收者
    # message['Cc'] = ''        # 抄送

    subject = 'Python SMTP 邮件测试'
    message['Subject'] = Header(subject, 'utf-8')

    try:
        smtpObj = smtplib.SMTP_SSL('smtp.qq.com', 465)
        smtpObj.login(EMAIL_ADDRESS, KEY)
        smtpObj.sendmail(sender, receivers, message.as_string())
        print('邮件发送成功')
    except smtplib.SMTPException:
        print('Error: 无法发送邮件')

send_email('这是一封测试邮件')