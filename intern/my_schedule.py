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

#每天启动爬虫的时间
time_str = "11:43"

def job():
    print("I'm working...")
    os.system('scrapy crawl sm')

# schedule.every(10).seconds.do(job)
# schedule.every(10).minutes.do(job)
# schedule.every().hour.do(job)
schedule.every().day.at(time_str).do(job)

while True:
    schedule.run_pending()
    time.sleep(1)