# -*- coding: utf-8 -*-
import scrapy
import urllib.request
from scrapy.http import Request,FormRequest

class LoginspdSpider(scrapy.Spider):
    name = 'loginspd'
    allowed_domains = ['douban.com']
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}

    def start_requests(self):
        return [Request ('https://www.douban.com/accounts/login',meta={'cookiejar':1},callback=self.parse,headers=self.headers)]

    def parse(self, response):
        captcha=response.xpath('//img[@id="captcha_image"]/@src').extract()

        if len(captcha) > 0:
            print('此时有验证码')
            localpath='D:/AuI18N/captcha.png'
            urllib.request.urlretrieve(captcha[0],filename=localpath)
            print('请查看图片，并输入验证码')
            captcha_value=input()
            data={
                "form_email":'13792453017',
                "form_password":'370284hao7',
                "captcha-solution":captcha_value,
                "redir":'https://www.douban.com/people/169085113/'
            }
        else:
            print('此时没有验证码')
            data={
                "form_email":'13792453017',
                "form_password":'370284hao7',
                "redir":'https://www.douban.com/people/169085113/',
            }
        print('登陆中......')
        return [FormRequest.from_response(response ,
                                        #  meta={'cookiejar':response.meta['cookiejar']},
                                         headers=self.headers,
                                         formdata=data,
                                         callback=self.next,
                                          ) ]
    def next(self,response):
        print('此时已登录完成并爬取了信息')
        xt='//*[@id="db-usr-profile"]/div[2]/h1/text()'
        title=response.xpath(xt).extract()
        print('网页标题是'+title[0])


