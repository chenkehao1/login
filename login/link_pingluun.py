import requests
import re
import json



#读取免费IP为列表
def jiansuo1():
    ku = []
    with open('D:/AuI18N/IP.txt', 'r', encoding='utf-8')as f:
        for line in f:
            i = json.loads(line)
            ku.append(i['ip'])
        return ku


#读取收费IP为列表
def jiansuo2():
     ku = []
     with open('D:/AuI18N/IP1.txt', 'r' ,encoding='utf-8')as f:
        for line in f:
            ku.append(line.replace('\n',''))
     return ku


#读取网址为列表
def jiansuo():
     ku = []
     with open('D:/AuI18N/虎啸龙吟/话题讨论.json', 'r' ,encoding='utf-8')as f:
        for line in f:
            i = json.loads(line)
            ku.append(i['url'])
     return ku


def qingxi():
    with open('D:/AuI18N/虎啸龙吟/评论.txt', 'r', encoding='utf-8') as f, open('D:/AuI18N/虎啸龙吟/评论31日.txt', 'w', encoding='utf-8') as f1:
        for lins in f:
            new = lins.replace('<p>', '')
            new = new.replace('</p>', '')
            new = new.replace('</span>', '')
            f1.write(new)




def main():
    item = jiansuo()
    path = '虎啸龙吟'
    url = 0
    i = 0
    t = jiansuo2()
    g = []
    headres = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1 QIHU 360SE '}
    while url < len(item):
        print('---------第'+str(i)+'次发送请求一级页面--------------------------------')
        IP = {'https': ''}
        print('剩余IP数量为'+str(len(t)))
        if t == []:
            t = jiansuo2()
            print('IP代理池更新完成')
        try:
            i += 1
            IP['https'] = 'http://'+t[0]
            print(IP)
            r = requests.get(item[url], proxies=IP, headers=headres,timeout=40)
            data1 = r.text
             #爬取每一个讨论的内容和话题评论内容

            biaoti = re.compile('<span class="">([\s\S]*?)<br clear="all"/>').findall(data1)
            huifu = re.compile('class="">(.*?)</p>') .findall(data1)
            pye = re.compile('author=0#comments" >(.*?)</a>').findall(data1)
            if biaoti != [] or huifu != []:
                print('正在读取内容......'+'第'+str(url)+'个网址')
                f = open('D:/AuI18N/'+path+'/评论2.2.txt', 'a', encoding='utf-8')
                url += 1
                #判断讨论标题如果为空就不写入标题直接进入回复评论的循环
                if biaoti != []:
                    f.write(biaoti[0])

                 #写入话题评论的第一页的回复内容
                for a in range(0, len(huifu)):
                    f.write(huifu[a])

                #如果话题评论有多页就循环爬取写入
                if len(pye)+1 >= 2:
                    bs = 100
                    j = len(pye) * 100
                    while bs < j:
                        print('第'+str(bs)+'条')
                        if t == []:
                            t = jiansuo2()
                            print('IP代理池更新完成')
                        try:
                            print('---------第'+str(i)+'次发送请求二级页面---')
                            i += 1
                            bs += 100
                            u = requests.get(item[url]+'?start='+str(bs), proxies=IP, headers=headres, timeout=60)
                            data2 = u.text
                            lint = re.compile('class="">(.*?)</p>').findall(data2)
                            #循环提取回复内容并写入文件
                            for c in range(0, len(lint)):
                                f.write(lint[c])
                        except Exception as e:
                            g.append(t[0])
                            del t[0]
                            IP['https'] = 'http://'+t[0]
                            bs -= 100
                            print('exception'+str(e), '本次结束更换IP')
            else:
                print(data1)
                h = input('是否选择重复爬取此王页，请输是或否')
                if h == '是':
                    g.append(t[0])
                    del t[0]
                else:
                    url += 1
        except Exception as e:
            g.append(t[0])
            del t[0]
            print('exception'+str(e), '本次结束')
    f.close()
    f = open('D:/AuI18N/过滤后IP.txt', 'w', encoding='utf-8')
    for i in range(len(g)):
        h = g[i] + '\n'
        f.write(h)
    f.close()





if __name__ == '__main__':
    qingxi()










'''
headres = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1 QIHU 360SE '}

for e in range(0, 601):
    print('---------第'+str(e)+'次发送请求--------------------------------')
    IP = {'https': ''}
    print('剩余IP数量为'+str(len(t)))
    if t == []:
        ipchi.ipchi()
        t = jiansuo2()
        print('IP代理池更新完成')
    try:
        IP['https'] = 'http://'+t[0]
        print(IP)
        r = requests.get("https://movie.douban.com/subject/26898192", proxies=IP, headers=headres,timeout=30)
        data = r.text
        i = re.compile('<span property="v:itemreviewed">(.*?)</span>').findall(data)
        if i == []:
            print(data)
        else:
            print(i, '爬取成功')
    except Exception as e:
        del t[0]
        print('exception'+str(e), '程序结束')
'''
