# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item, Field 



class  Article(Item):
    zhuanlan = Field() #所属专栏
    title = Field() #文章主题
    site = Field() #文章地址
    content = Field()  #内容
    author = Field() #
    star = Field() #点赞数量

#class (scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
