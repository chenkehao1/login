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
    #定义首次爬取网址
    def start_requests(self):
        yield Request('https://movie.douban.com/subject/27087788/discussion/',headers=
        {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'})
    #评论循环计数器
    y = 0

    def parse(self, response):
        itme = LoginItem()
        #爬取评论总页数
        t = response.xpath('//*[@id="content"]/div/div[1]/div[3]/span[2]/@data-total-page').extract()
        for i in range(0, int(t[0])):
            #爬取话题标题和链接
            self.y += 20
            time.sleep(3)
            data = urllib.request.urlopen('https://movie.douban.com/subject/27087788/discussion/?start='+str(self.y)).read().decode('utf-8')
            itme['name'] = re.compile('title="(.*?)"').findall(data)
            itme['user'] = re.compile('<a href="https://www.douban.com/.*?" class="">([\s\S]*?)</td>').findall(data)
            itme['url'] = re.compile('<a href="(.*?)" title="').findall(data)
            itme['hy'] = re.compile('<td>(.*?)</td').findall(data)
            itme['sj'] = re.compile(' <td class="time">(.*?)</td>').findall(data)

            for ts in range(0, len(itme['url'])):
                #爬取每一个讨论的内容和话题评论内容
                time.sleep(4)
                data1 = urllib.request.urlopen(itme['url'][ts]).read().decode('utf-8')
                t1 = re.compile('<span class="">([\s\S]*?)<br clear="all"/>').findall(data1)
                t2 = re.compile('class="">(.*?)</p>') .findall(data1)
                t3 = re.compile('author=0#comments" >(.*?)</a>').findall(data1)
                f = open('D:/AuI18N/虎啸龙吟/1.txt', 'a', encoding='utf-8')

                #判断讨论标题如果为空就不写入
                if t1 != []:
                    f.write(t1[0])

                 #写入话题评论的第一页内容
                for a in range(0, len(t2)):
                    f.write(t2[a])

                #如果话题评论有多页就循环爬取写入
                if len(t3)+1 >= 2:
                    b1 = 0
                    for b in range(0, len(t3)+1):
                        time.sleep(5)
                        b1 += 100
                        data2 = urllib.request.urlopen(itme['url'][ts]+'?start='+str(b1)).read().decode('utf-8')
                        b2 = re.compile('class="">(.*?)</p>').findall(data2)
                        for c in range(0, len(b2)):
                            f.write(b2[c])
                f.close()

            yield itme

