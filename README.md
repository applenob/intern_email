# intern_email
## 1.introduce
爬取实习信息（[水木社区](http://www.newsmth.net/nForum/#!board/Intern)），归类并评分，将自己感兴趣的实习信息发送至邮箱。
介绍爬虫的[blog](http://www.jianshu.com/p/35c0830448c2)
目前只有三种实习信息分类：开发/算法/金融
## 2.部署
安装mongodb，并启动。
```
mongod -dbpath /path/of/your/db
```
安装第三方python包
```
pip install bs4, scrapy, selenium, pymongo, schedule
```
安装phantomjs，去[官网](http://phantomjs.org/download.html)下载
## 3.启动
```
cd intern
python my_schedule.py
```
在服务器端部署：
```
nohup python my_schedule.py > sm_log.txt 2>1& &
```
输入自己的126邮箱和密码（以支持126的SMTP邮件转发服务），想修改为其他邮箱，需要修改其他SMTP的服务器地址。
## 4.个性化
修改目的邮箱：
在文件intern/send_2_email.py中，找到receivers列表，修改目的邮箱即可。
修改每天启动任务的时间：
在文件intern/my_schedule.py中，修改time_str为你需要的时间。
个性化自己的评分标准：
在文件intern/pipeline.py中，找到：
```
important_key_dict = {
            'NLP':5,
            'nlp':5,
            '自然语言处理':5,
            '文本挖掘': 5,
            'Spark':5,
            'spark':5,
            'LSTM':5,
            'lstm':5,
            'word2vec':5,
            'Tensorflow':5,
            'tensorflow': 5,
            '机器学习':4,
            '深度学习':4,
            '数据挖掘':4,
            '推荐':4,
            '文本分析': 4,
            '情感识别':4,
            '计算广告': 3,
            'python':3,
            'scala':3,
            '住房补贴':2,
            '房补':2,
        }
```
自己修改关键词，以及相应的权重，不限个数。
## 5.效果
![](https://github.com/applenob/intern_email/resource/email.png)
