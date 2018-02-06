#！/usr/bin/env python
#-*-coding:utf-8-*-
# chenkehao
import urllib.request
import re
import json
import urllib.parse
import matplotlib.pyplot as plt
import pandas
from pylab import mpl

#更新剧库
def oa():
    par = '"title":"(.*?)"'
    par1 = '"url":"(.*?)/"'
    par2 = '"rate":"(.*?)"'
    type1 = ['美剧', '英剧', '韩剧', '日剧', '国产剧', '港剧', '日本动画', '综艺', '纪录片']
    with open('D:/AuI18N/片库.json', 'w', encoding='utf-8')as f:
        for i in range(0, len(type1)):
            t = []
            j = urllib.parse.quote(type1[i])
            data = urllib.request.urlopen(
                    'https://movie.douban.com/j/search_subjects?type=tv&tag='+str(j)+'&page_limit=10000&page_start=0'
            ).read().decode('utf-8')
            list1 = re.compile(par).findall(data)
            list2 = re.compile(par1).findall(data)
            list3 = re.compile(par2).findall(data)
            print(type1[i], len(list1))
            for a in range(0, len(list2)):
                t.append(list2[a].replace('\\', ''))
            for b in range(0, len(list1)):
                    name = list1[b]
                    url = t[b]
                    fs = list3[b]
                    g = {name: {'url': url, '评分': fs, 'type': type1[i]}}
                    j = json.dumps(dict(g), ensure_ascii=False)
                    h = j + '\n'
                    f.write(h)


#将剧种分类并计算平均分
def jisuan():
    j = {'美剧': '', '英剧': '', '韩剧': '', '日剧': '', '国产剧': '', '港剧': '', '日本动画': '', '综艺': '', '纪录片': ''}
    with open('D:/AuI18N/片库.json', 'r', encoding='utf-8') as f:
        for lint in f:
            i = json.loads(lint)
            for key in i:
                if i[key]['type'] == '美剧':
                    j['美剧'] = str(eval(j['美剧'] +'+'+ i[key]['评分']))
                elif i[key]['type'] == '英剧':
                    j['英剧'] = str(eval(j['英剧'] +'+'+ i[key]['评分']))
                elif i[key]['type'] == '韩剧':
                    j['韩剧'] = str(eval(j['韩剧'] +'+'+ i[key]['评分']))
                elif i[key]['type'] == '日剧':
                    j['日剧'] = str(eval(j['日剧'] +'+'+ i[key]['评分']))
                elif i[key]['type'] == '国产剧':
                    j['国产剧'] = str(eval(j['国产剧'] +'+'+ i[key]['评分']))
                elif i[key]['type'] == '港剧':
                    j['港剧'] = str(eval(j['港剧'] +'+'+ i[key]['评分']))
                elif i[key]['type'] == '日本动画':
                    j['日本动画'] = str(eval(j['日本动画'] +'+'+ i[key]['评分']))
                elif i[key]['type'] == '综艺':
                    j['综艺'] = str(eval(j['综艺'] +'+'+ i[key]['评分']))
                else:
                    j['纪录片'] = str(eval(j['纪录片'] +'+'+ i[key]['评分']))
        for key in j:
            if key == '英剧':
                j[key] = round(eval(j[key] +'/'+ '397'), 2)
                continue
            j[key] = round(eval(j[key] +'/'+ '500'), 2)
    return j


#分析数据并作图
def fenxi(fen, biaoqian):
    mpl.rcParams['font.sans-serif'] = ['Microsoft YaHei']   # 指定默认字体：解决plot不能显示中文问题
    mpl.rcParams['axes.unicode_minus'] = False

    data = pandas.Series(fen, index=biaoqian)
    data.plot(kind='barh', grid=True, xticks=[1, 2, 3, 4, 5, 6, 7, 8, 9])
    plt.show()



def main():
    i = jisuan()
    fen = []
    biaoqian = []
    #循环遍历字典的键-值添加进列表
    for key, value in i.items():
        fen.append(value)
        biaoqian.append(key)
    fenxi(fen, biaoqian)



if __name__ == '__main__':
    main()