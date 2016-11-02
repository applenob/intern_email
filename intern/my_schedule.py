#coding=utf-8
'''
每天固定时间启动爬虫
部署在服务器下可以使用以下命令：
nohup python my_schedule.py > sm_log.txt 2>1& &
数据库要确保标题是unique的，打开mongo，输入：
db.items.ensureIndex({'title':1},{unique:true})
'''

import schedule
import time
import os
import send_2_email

#每天启动爬虫的时间
time_str = "16:11"
mail_user = ''
mail_pass = ''


def job():
    print("I'm working...")
    # 启动爬虫
    os.system('scrapy crawl sm')
    # 从数据库获取最新信息
    infos = send_2_email.query_info()
    # 发送邮件
    send_2_email.send_email(infos, mail_user, mail_pass)

# schedule.every(10).seconds.do(job)
# schedule.every(10).minutes.do(job)
# schedule.every().hour.do(job)
if __name__ == '__main__':
    mail_user = raw_input("input SMTP username (using 126 SMTP service):")
    import getpass
    mail_pass = getpass.getpass()
    schedule.every().day.at(time_str).do(job)

    while True:
        schedule.run_pending()
        time.sleep(1)