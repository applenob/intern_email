#coding=utf-8
import time
import pymongo
import settings
# print time.strftime('%Y-%m-%d',time.localtime(time.time()))
# print '<tr><a href="{item_url}">{item_title}</a></tr>'\
#             .format(item_url=123,item_title=456)

def mongodb_test():
    client = pymongo.MongoClient(
        settings.MONGODB_SERVER,
        settings.MONGODB_PORT
    )
    db = client[settings.MONGODB_DB]
    collection = db[settings.MONGODB_COLLECTION]
    result = collection.find({'title':"123"}).count()
    print result

if __name__ == '__main__':
    mongodb_test()