# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo

# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from myrss.items import IpsPool


class MyrssPipeline:
    def __init__(self, mongo_url, mongo_db):
        self.mongo_url = mongo_url
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_url=crawler.settings.get('MONGO_URL'),
            mongo_db=crawler.settings.get('MONGO_DB')
        )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_url)
        self.db = self.client[self.mongo_db]

    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        print(dict(item))
        if isinstance(item, IpsPool):
            collection = self.db['ips']
            condition = {'agency': item['agency']}
            queryRes = collection.find_one(condition)
            if queryRes:
                collection.update(condition, dict(item))
            else:
                collection.insert(dict(item))
            return item
