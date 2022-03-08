# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanItem(scrapy.Item):
    # define the fields for your item here like:
     name_list = scrapy.Field()
     grade_list = scrapy.Field()
     pj_list=scrapy.Field()
     id_list=scrapy.Field()
