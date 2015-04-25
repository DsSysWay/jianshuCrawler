# -*- coding: utf-8 -*-
from __future__ import unicode_literals
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


from scrapy import signals
import json
import codecs
import sys
reload(sys)
sys.setdefaultencoding('utf-8')



class JianshuPipeline(object):
    counter = 0;
    def process_item(self, item, spider):
        title = item['title']

        if(title == None):
            title = str(self.counter)
            self.counter = self.counter + 1
            ###  下面如果title是中文和英文拼接会出现问题的
        tmpFile = codecs.open(title, 'w', encoding='utf-8')
        content = item['content'].encode("utf-8")
        tmpFile.write(content)
        tmpFile.flush()
        tmpFile.close()
        return item


