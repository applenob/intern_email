#coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('UTF8')
'''
将有用的实习信息，以邮件的形式转发给我，每天一封
'''
import settings
import pymongo
import smtplib
from email.mime.text import MIMEText
from email.header import Header
import datetime
import getpass


def query_info():
    '''从mongodb中查询数据'''
    client = pymongo.MongoClient(
        settings.MONGODB_SERVER,
        settings.MONGODB_PORT
    )
    db = client[settings.MONGODB_DB]
    collection = db[settings.MONGODB_COLLECTION]
    today = datetime.datetime.today()
    # 查询属于算法类且推荐指数大于0且收集日期为今天的数据，按照推荐指数，降序排列
    return collection.find({"is_alg": True, 'collect_time': today.strftime('%Y-%m-%d'),
                            'recommend_level': {'$gt': 0}}).sort([("recommend_level", -1)])


def send_email(infos, mail_user='', mail_pass=''):
    '''封装信息，发送邮件'''
    print
    print "开始发送邮件"
    # 第三方SMTP服务
    mail_host = 'smtp.126.com' # 使用126的SMTP服务
    # 手动输入用户名和密码
    if mail_user == '':
        mail_user = raw_input("input SMTP username (using 126 SMTP service):")
    if mail_pass == '':
        mail_pass = getpass.getpass()

    sender = mail_user
    receivers = ['nobking@126.com']  # 接收邮件，可设置为你自己的邮箱

    html_content = """
    <h1>水木社区实习信息 {send_date}</h1>
    <h2>今日更新实习</h2>
    <body>
    <table>
        <tbody>
    """.format(send_date=datetime.datetime.today().strftime('%Y-%m-%d'))

    num = 0
    base_url = 'http://www.newsmth.net'
    for info in infos:
        html_content += ' <tr><h3><a href="{item_url}">{item_title}</h3>'\
            .format(item_url=base_url+info['href'],item_title=info['title'])
        html_content += '<p>{content}</p>'.format(content=info['content'])
        html_content += '<h3>推荐指数：{recommend_level}</h3></tr>'.format(recommend_level=info['recommend_level'])
        num += 1
    html_content += '''
    </tbody>
    </table>
    <p>一共{item_num}条</p>
    </body>
    '''.format(item_num=num)

    message = MIMEText(html_content, 'html', 'utf-8')
    message['From'] = Header("Cer", 'utf-8')
    message['To'] = Header("Intern Receiver", 'utf-8')

    subject = '{send_date}实习摘要'.format(send_date=datetime.datetime.today().strftime('%Y-%m-%d'))
    message['Subject'] = Header(subject, 'utf-8')

    try:
        smtpObj = smtplib.SMTP()
        smtpObj.connect(mail_host, 25) #默认端口25
        smtpObj.login(mail_user, mail_pass)
        smtpObj.sendmail(sender, receivers, message.as_string())
        print "邮件发送成功"
    except smtplib.SMTPException as e:
        print "Error: 无法发送邮件"
        print e

if __name__ == '__main__':
    infos = query_info()
    send_email(infos)
