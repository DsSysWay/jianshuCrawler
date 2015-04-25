# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item, Field 



class  Article(Item):
    title = Field() #文章主题
    url = Field() #文章地址
    content = Field()  #内容

#class (scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
