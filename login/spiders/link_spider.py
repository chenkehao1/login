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
    url = ''
    path = ''
    #定义首次爬取网址
    def start_requests(self):
        yield Request(self.url+'/discussion/',headers=
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
            data = urllib.request.urlopen(self.url+'/discussion/?start='+str(self.y)).read().decode('utf-8')
            itme['name'] = re.compile('title="(.*?)"').findall(data)
            itme['user'] = re.compile('<a href="https://www.douban.com/.*?" class="">([\s\S]*?)</td>').findall(data)
            itme['url'] = re.compile('<a href="(.*?)" title="').findall(data)
            itme['hy'] = re.compile('<td>(.*?)</td').findall(data)
            itme['sj'] = re.compile(' <td class="time">(.*?)</td>').findall(data)

            for ts in range(0, len(itme['url'])):
                #爬取每一个讨论的内容和话题评论内容
                time.sleep(4)
                data1 = urllib.request.urlopen(itme['url'][ts]).read().decode('utf-8')
                biaoti = re.compile('<span class="">([\s\S]*?)<br clear="all"/>').findall(data1)
                huifu = re.compile('class="">(.*?)</p>') .findall(data1)
                pye = re.compile('author=0#comments" >(.*?)</a>').findall(data1)
                f = open('D:/AuI18N/'+self.path+'/评论.txt', 'a', encoding='utf-8')

                #判断讨论标题如果为空就不写入标题直接进入回复评论的循环
                if biaoti != []:
                    f.write(biaoti[0])

                 #写入话题评论的第一页的回复内容
                for a in range(0, len(huifu)):
                    f.write(huifu[a])

                #如果话题评论有多页就循环爬取写入
                if len(pye)+1 >= 2:
                    bs = 0
                    for b in range(0, len(pye)+1):
                        time.sleep(5)
                        bs += 100
                        data2 = urllib.request.urlopen(itme['url'][ts]+'?start='+str(bs)).read().decode('utf-8')
                        lint = re.compile('class="">(.*?)</p>').findall(data2)
                        #循环提取回复内容并写入文件
                        for c in range(0, len(lint)):
                            f.write(lint[c])
                f.close()
            yield itme

