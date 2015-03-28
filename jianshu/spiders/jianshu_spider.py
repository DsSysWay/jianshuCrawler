#coding="utf-8"
import  re
import json


from scrapy.selector import Selector
try:
    from scrapy.spider import Spider
except:
    from scrapy.spider import BaseSpider as Spider
from scrapy.utils.response import get_base_url
from scrapy.utils.url import urljoin_rfc
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor as sle


from jianshu.items import *
from jianshu.misc.log import *
import codecs

file_object = codecs.open("log.txt","w","utf-8")
items = []

class jianshuSpider(CrawlSpider):

    name = "jianshu" #here is the key to name spider,if not match will throw spider not found error
    allowed_domains = ["tencent.com"]
    start_urls = [
            "http://www.jianshu.com/collections?category_id=8&_=1427558117311"
            #program zhuan lan
    ]
    rules = [
        Rule(sle(allow=("/collection/[0-10a-zA-Z]+")), follow=True, callback='parse_zhuanlan'),
        Rule(sle(allow=("/p/[0-10a-zA-Z]+")), follow=True, callback='parse_item')
    ]

    def parse_zhuanlan(self, response):
        info("jianshu zhuanlan"+ str(response));
        return response;

    def parse_item(self, response):
        sel = Selector(response)
        base_url = get_base_url(response)
        sites_even = sel.css('container')
        item = Article()
        # item['name'] = site.css('.l.square a').xpath('text()').extract()[0]
        # relative_url = site.css('.l.square a').xpath('@href').extract()[0]
        # item['detailLink'] = urljoin_rfc(base_url, relative_url)
        # item['catalog'] = site.css('tr > td:nth-child(2)::text').extract()[0]
        # item['workLocation'] = site.css('tr > td:nth-child(4)::text').extract()[0]
        # item['recruitNumber'] = site.css('tr > td:nth-child(3)::text').extract()[0]
        # item['publishTime'] = site.css('tr > td:nth-child(5)::text').extract()[0]
        item['zhuanlan'] = ""
        item['title']    = site.css('title').xpath('text()').extract()[0]
        item['author']    = site.css('meta-top > span:nth-child(1)::text').extract()[0]
        item['content']    = site.css('show-content').xpath('text()').extract()[0]
        item['star']    = site.css('like-content').xpath('text()').extract()[0]
        item['site']     =  "" 
        items.append(item)
            #print repr(item).decode("unicode-escape") + '\n'

        return items


    def _process_request(self, request):
        info('process ' + str(request))
        return request

