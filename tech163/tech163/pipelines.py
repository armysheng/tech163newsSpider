# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
#encoding: utf-8
from store import NewsDB

class Tech163Pipeline(object):
    def process_item(self, item, spider):
        if spider.name != "news":  return item
        if item.get("news_thread", None) is None: return item

        # spec = { "title": item["title"] }
        # NewsDB.tech163.insert(spec, {'$set': dict(item)}, upsert=True)
        # NewsDB.tech163.save({'news_title':news_title,'news_time':news_time,'news_from':news_from,'from_url':from_url,'news_body':news_body})
        # NewsDB.tech163.insert(item)
        spec = { "news_thread": item["news_thread"] }
        NewsDB.news.update(spec, {'$set': dict(item)}, upsert=True)

        return None
        



# class MoviePipeline(object):
#     def process_item(self, item, spider):
#         if spider.name != "movie":  return item
#         if item.get("subject_id", None) is None: return item

#         spec = { "subject_id": item["subject_id"] }
#         doubanDB.movie.update(spec, {'$set': dict(item)}, upsert=True)

#         return None
