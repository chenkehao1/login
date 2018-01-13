# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.

import linkspider

if __name__ == '__main__':
    st = input('是否更新影视库,请输入是与否：')
    if st == '是':
        linkspider.oa()


