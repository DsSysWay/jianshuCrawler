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
import sys
reload(sys)
sys.setdefaultencoding('utf-8')



###URL2_ARTICLE_TITLE = {}
class jianshuSpider(CrawlSpider):

    name = "jianshu" #here is the key to name spider,if not match will throw spider not found error
    allowed_domains = ["jianshu.com"]
    start_urls = [
            "http://www.jianshu.com/collections?category_id=8&order_by=score&_=1429111447249&page=1"
            #program zhuan lan
    ]
    rules = [
        Rule(sle(allow=("collections?category_id=8&order_by=score&_=1429111447249&page=[0-9]+")), follow=True, callback='parse_zhuanlan'),
        Rule(sle(allow=("/collection/[0-10a-zA-Z]+")), follow=True, callback='parse_article_list'),
        Rule(sle(allow=("/p/[0-10a-zA-Z]+")), follow=True, callback='parse_article')
    ]


    max_page_limit = 10

    def constructNextZhuanlanUrl(self,url):
        length  = len(url)
        page_num = url[length-1]
        if(page_num < 15):
            page_num = page_num + 1
            url[length-1] = page_num
            return url
        return ""

    def extractContentFromAElement(self,content):
        length = len(content)
        if(length > 1):
            return content[1:(length-4)]

    def parse_zhuanlan(self, response):
        info("zhuanlan url:"+response.url)
        base_url = get_base_url(response)
        selectorList = response.xpath("//h5/a[contains(@href,'collection')]")
        for   selector in selectorList:
            hrefStr = selector.extract()
            hrefList = hrefStr.split("\"")
            href = base_url + hrefList[1]
            info("article list href  str:"+ href)
            name = self.extractContentFromAElement(hrefList[2])
            info("zhuanlan name:" + name)
            yield  scrapy.Request(href,self.parse_article_list)
        next_zhuanlan_page = self.constructNextZhuanlanUrl(response.url)
        if(len(next_zhuanlan_page) != 0):
            info("next zhuanlan page:"+next_zhuanlan_page)
            yield  scrapy.Request(href,self.parse_zhuanlan)


    def parse_article_list(self, response):
        global URL2_ARTICLE_TITLE
        info("parse article list  url:"+response.url)
        base_url = get_base_url(response)
        selectorList = response.xpath("//h4/a[contains(@href,'p')]")
        for selector in selectorList:
            hrefStr = selector.extract()
            hrefList = hrefStr.split("\"") 
            href = base_url + hrefList[1]
            info("article href:"+href)
            name = self.extractContentFromAElement(hrefList[4])
            name = name.encode("utf-8")
            ###URL2_ARTICLE_TITLE[href] = name
            yield  scrapy.Request(href,self.parse_article)



    def parse_article(self, response):
        article = Article()
###        base_url = get_base_url(response)
  ###      post_fix_len = len("?utm_campaign=maleskine&utm_content=note&utm_medium=pc_all_hots&utm_source=recommendation")
      ###  url = response.url[0:post_fix_len]
        url = response.url
        title = response.xpath("//h1[@class='title']/text()").extract()
        article['title'] = title[0].encode("utf-8")
        info("article name:"+ article['title'] )
        article['content']  = response.body
        article["url"]  = response.url
        return article

    def _process_request(self, request):
        info('process ' + str(request))
        return request

