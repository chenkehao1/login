# -*- coding: utf-8 -*-
import scrapy
import urllib.request

class DoubanysSpider(scrapy.Spider):
    name = 'doubanys'
    allowed_domains = ['douban.com']

    def parse(self, response):
        data=urllib.request.urlopen('https://movie.douban.com/j/search_subjects?type=tv&tag=%E7%83%AD%E9%97%A8&page_limit=100&page_start=0').read()
        print(data)

