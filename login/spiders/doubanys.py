# -*- coding: utf-8 -*-
import scrapy
import urllib.request
import json
class DoubanysSpider(scrapy.Spider):
    name = 'doubanys'
    allowed_domains = ['douban.com']
    i = json.load(open('D:/AuI18N/虎啸龙吟/12.json', 'r'))

    def parse(self, response):
        pass



