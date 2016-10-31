#coding=utf-8
import time
# print time.strftime('%Y-%m-%d',time.localtime(time.time()))
print '<tr><a href="{item_url}">{item_title}</a></tr>'\
            .format(item_url=123,item_title=456)