# -*- coding: utf-8 -*-
import scrapy
from login.items import LoginItem
from scrapy.http import Request
import re
import urllib.request
import time
class LinkSpiderSpider(scrapy.Spider):
    name = 'link_spider'
    allowed_domains = ['douban.com']
    def start_requests(self):
        yield Request('https://movie.douban.com/subject/27087788'+'/discussion/',headers=
            {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'})
    y = 0
    def parse(self, response):
        itme = LoginItem()
        t = response.xpath('//*[@id="content"]/div/div[1]/div[3]/span[2]/@data-total-page').extract()
        data = response.text
        itme['name'] = re.compile('title="(.*?)"').findall(data)
        itme['user'] = re.compile('<a href="https://www.douban.com/.*?" class="">([\s\S]*?)</td>').findall(data)
        itme['url'] = re.compile('<a href="(.*?)" title="').findall(data)
        itme['hy'] = re.compile('<td>(.*?)</td').findall(data)
        itme['sj'] = re.compile(' <td class="time">(.*?)</td>').findall(data)

        for ts in range(0, len(itme['url'])):
            time.sleep(5)
            data1 = urllib.request.urlopen(itme['url'][ts]).read().decode('utf-8')
            t1 = re.compile('<span class="">([\s\S]*?)<br clear="all"/>').findall(data1)
            t2 = re.compile('class="">(.*?)</p>') .findall(data1)
            t3 = re.compile('author=0#comments" >(.*?)</a>').findall(data1)
            f = open('D:/AuI18N/虎啸龙吟/1.txt', 'a', encoding='utf-8')
            if t1 != []:
                f.write(t1[0])
            for a in range(0, len(t2)):
                f.write(t2[a])
            if len(t3)+1 >= 2:
                b1 = 0
                for b in range(0, len(t3)+1):
                    time.sleep(2)
                    b1 += 100
                    data2 = urllib.request.urlopen(itme['url'][ts]+'?start='+str(b1)).read().decode('utf-8')
                    b2 = re.compile('class="">(.*?)</p>').findall(data2)
                    for c in range(0, len(b2)):
                        f.write(b2[c])
            f.close()

        yield itme



        for i in range(0,2):
            self.y += 20
            print(i)
            time.sleep(15)
            yield Request('https://movie.douban.com/subject/27087788/discussion/?start='+str(self.y), callback=self.parse,
                headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'})
