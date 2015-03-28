# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


from scrapy import signals
import json
import codecs



class JianshuPipeline(object):
    def process_item(self, item, spider):
        tmpFile = codecs.open("./article/"+item['title']+".txt", 'w', encoding='utf-8')
        content = json.dumps(dict(item), ensure_ascii=False) + "\n"
        tmpFile.write(content)
        tmpFile.flush();
        tmpFile.close();
        return item


