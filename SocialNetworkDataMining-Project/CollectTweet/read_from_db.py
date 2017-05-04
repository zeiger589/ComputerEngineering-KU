from mongo_auth import *
import pymongo
import json
from pymongo import MongoClient
from bson.json_util import dumps
import unicodedata
import string
import sys

reload(sys)
sys.setdefaultencoding('utf8')

if __name__ == '__main__':
    client = MongoClient('mongodb://' + MONGO_USERNAME + ':' + MONGO_PASSWORD
                         + '@watcharaphat.com')
    db = client['twitter_db']
    collection = db['good_tweets']

    cursor = collection.find(
        {},
        {"text": 1, "_id": 0}
    )

    i = 0
    for document in cursor:
        if (i < 100):
            print dumps(document, ensure_ascii=False)
            i = i + 1
        else:
            sys.exit()
