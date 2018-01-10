# -*- coding: utf-8 -*-
import scrapy
from login.items import LoginItem
from scrapy.http import Request

class LinkSpiderSpider(scrapy.Spider):
    name = 'link-spider'
    allowed_domains = ['douban.com']
    def start_requests(self):
        yield Request('https://movie.douban.com/subject/27087788'+'/discussion/',headers=
            {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'})
    y = 0
    def parse(self, response):
        itme = LoginItem()
        t = response.xpath('//*[@id="content"]/div/div[1]/div[3]/span[2]/@data-total-page').extract()
        itme['name'] = response.xpath('//*[@id="posts-table"]/tbody/tr[2]/td[1]/a/@href').extract()
        print(itme['name'])
        '''
        itme['user'] = response.xpath('').extract()
        itme['url'] = response.xpath('').extract()
        itme['hy'] = response.xpath('').extract()
        itme['sj'] = response.xpath('').extract()


        for i in range(int(t[0])+1):
            self.y += 20
            yield Request('https://movie.douban.com/subject/27087788/discussion/?start='+str(self.y),headers=
            {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'})
'''