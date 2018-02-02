# -*- coding: utf-8 -*-
import scrapy
from login.items import LoginItem
from scrapy.http import Request
import re
import urllib.request
import urllib.parse
import http.cookiejar
import time

class LinkSpiderSpider(scrapy.Spider):
    name = 'link_spider'
    allowed_domains = ['douban.com']
    url = 'https://movie.douban.com/subject/27087788'
    path = '虎啸龙吟'
    #定义首次爬取网址
    def start_requests(self):
        yield Request('https://movie.douban.com/subject/27087788/discussion/', headers=
        {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'})

    #评论循环计数器
    y = 0

    def parse(self, response):
        item = LoginItem()
        #爬取评论总页数
        t = response.xpath('//*[@id="content"]/div/div[1]/div[3]/span[2]/@data-total-page').extract()
        print(t)
        url='https://www.douban.com/accounts/login'#'https://weibo.com/liuyifeiofficial?page=1'
        p=urllib.parse.urlencode({
        "form_email":'13792453017',
        "form_password":'370284hao7'
            }).encode('utf-8')
        r=urllib.request.Request(url,p)
        r.add_header=('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36')
        c=http.cookiejar.CookieJar()
        op=urllib.request.build_opener(urllib.request.HTTPCookieProcessor(c))
        urllib.request.install_opener(op)

        try:
            for i in range(0, int(t[0])):

                #爬取话题标题和链接

                print(self.y)
                r = urllib.request.Request(self.url+'/discussion/?start='+str(self.y),p)
                r.add_header=('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36')
                data = urllib.request.urlopen(r,timeout=5).read().decode('utf-8')
                item['name'] = re.compile('title="(.*?)"').findall(data)
                item['user'] = re.compile('<a href="https://www.douban.com/.*?" class="">([\s\S]*?)</td>').findall(data)
                item['url'] = re.compile('<a href="(.*?)" title="').findall(data)
                item['hy'] = re.compile('<td>([\d]*)</td').findall(data)
                item['sj'] = re.compile(' <td class="time">(.*?) [\d]+:[\d]+</td>').findall(data)
                self.y += 20
                yield item
        except Exception as e:
            url='https://www.douban.com/accounts/login'#'https://weibo.com/liuyifeiofficial?page=1'
            p=urllib.parse.urlencode({
            "form_email":'13792453017',
            "form_password":'370284hao7'
                }).encode('utf-8')
            r=urllib.request.Request(url,p)
            r.add_header=('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36')
            c=http.cookiejar.CookieJar()
            op=urllib.request.build_opener(urllib.request.HTTPCookieProcessor(c))
            urllib.request.install_opener(op)
            print('exception'+str(e),'程序结束')


