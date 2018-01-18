#！/usr/bin/env python
#-*-coding:utf-8-*-
# chenkehao
import urllib.request
import re
import json
import urllib.parse
import os
import csv

#更新剧库
#在查找片库文件是，还是用正则匹配文件中的条目，然后把返回的值再用json格式化成字典，或者不格式化也可以，看哪种更简单效果更好
def oa():
    jis = 0
    par = '"title":"(.*?)"'
    par1 = '"url":"(.*?)/"'
    par2 = '"rate":"(.*?)"'
    type1 = ['美剧', '英剧', '韩剧', '日剧', '国产剧', '港剧', '日本动画', '综艺', '纪录片']
    with open('D:/AuI18N/pk.csv', 'w', encoding='utf-8')as f:
        wr = csv.writer(f)
        wr.writerow(('name', '评分', 'type'))
        for i in range(0, len(type1)):
            t = []
            j = urllib.parse.quote(type1[i])
            data = urllib.request.urlopen(
                    'https://movie.douban.com/j/search_subjects?type=tv&tag='+str(j)+'&page_limit=10000&page_start=0'
            ).read().decode('utf-8')
            list1 = re.compile(par).findall(data)
            list2 = re.compile(par1).findall(data)
            list3 = re.compile(par2).findall(data)
            print(type1[i],len(list1))
            for a in range(0, len(list2)):
                t.append(list2[a].replace('\\', ''))
            for b in range(0, len(list1)):
                #在写入数据库是name中如果出现英文逗号就会报错导致程序异常退出，所以这里加一段异常捕捉
                try:
                    name = list1[b]
                    url = t[b]
                    fs = list3[b]
                    #g = {name: {'url': url, '评分': fs, 'type': type1[i]}}
                    #j = json.dumps(dict(g), ensure_ascii=False)
                    #h = j + '\n'
                    #f.write(h)
                    wr.writerow((jis, name, fs, type1[i]))
                    jis += 1
                except Exception as e:
                    print('exception:'+str(e))

def jianso():
    ku = {}
    with open('D:/AuI18N/1.json', 'r' ,encoding='utf-8')as f:
        for line in f:
            i = json.loads(line)
            ku.update(i)
    return ku




#purl('https://movie.douban.com/subject/27087788/')


#将保存的字符串序列化为基本数据类型
#i=json.load(open('D:/AuI18N/虎啸龙吟/12.json','r'))#格式化输出
#print(i)


