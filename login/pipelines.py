# -*- coding: utf-8 -*-
import json
import codecs
import csv
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class LoginPipeline(object):
    def __init__(self):
        #刚开始链接时对应的数据库
        self.f = open('D:/AuI18N/虎啸龙吟/话题讨论.json', 'w', encoding='utf-8')
        #self.wr = csv.writer(self.f)
        #self.wr.writerow(('name', 'user', 'url', '回复', '时间'))

    def process_item(self, item, spider):

        print('111111')
        for j in range(0, len(item['url'])):
            name = item['name'][j]
            user = item['user'][j]
            url = item['url'][j]
            #if item['hy'][j] == '':
               # hy = '0'
            #else:
            hy = item['hy'][j]
            sj = item['sj'][j]
            g = {'标题': name, 'url': url, '账户名': user, '回复数': hy, '发布时间': sj}
            i = json.dumps(dict(g), ensure_ascii=False)
            h = i+'\n'
            print(h)
            self.f.write(h)
            print('111111')
            #self.wr.writerow((name, user, url, hy, sj))
        return item
    def close_spider(self):
        self.f.close()