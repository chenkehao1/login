# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.

import linkspider
import os

if __name__ == '__main__':
    st = input('如果要更新影视库,请输入‘是’：')
    if st == '是':
        linkspider.oa()
    ku = linkspider.jianso()
    name = input('请输入要查询的电视剧名：')
    url = ku.get(name)
    print(url)
    if url != None:
        os.makedirs(os.path.join('D:/AuI18N/', name))

