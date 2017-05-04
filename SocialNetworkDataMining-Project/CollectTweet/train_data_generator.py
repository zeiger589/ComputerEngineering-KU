# -*- coding: utf-8 -*-
from mongo_auth import *
import pymongo
import json
from pymongo import MongoClient
from bson.json_util import dumps
import unicodedata
import string
import sys
from textblob.classifiers import NaiveBayesClassifier

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

    train = []

    i = 0
    for document in cursor:
        if (i < 20000):
            s = unicodedata.normalize('NFKD', document.get('text')).encode('ascii','ignore')
            train.append( ( s, 'neg' ) )
            i = i + 1
        else:
            for item in train:
                print item
            sys.exit()
