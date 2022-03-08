# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from douban.items import DoubanItem
import pymysql


class DoubanPipeline(object):
    def __init__(self):
        self.db = pymysql.connect(host='localhost', user='nyk', passwd='123456', db='moveis', charset='utf8',
                                  port=3306)
        self.cur = self.db.cursor()

    def process_item(self, item, spider):
        sql = 'INSERT INTO douban_movies(id,name,pingjia,grade) VALUES("%s","%s","%s","%s")' % (
            item["id_list"], item["name_list"], item["pj_list"], item["grade_list"])
        self.cur.execute(sql)
        self.db.commit()
        return item

    def close_spider(self, spider):
        self.cur.close()
        self.db.close()
