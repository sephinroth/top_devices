#encoding=utf-8

import string
import urllib2
import datetime
import codecs
from lxml import etree

class HuiHui:
    def __init__(self):
        self.url = 'http://www.huihui.cn/web/search?q='

    def pquery(self, keyword):
        qstring = self.url + "+".join(string.split(keyword, ' '))
        content = urllib2.urlopen(qstring.encode('utf-8'))

        source_html = content.read()
        tree = etree.HTML(source_html)
        if len(tree.xpath("//div[@id='scRecommend']/div/div[@class='noresult']")) != 0:
            print 'NO result is found'
            return None, None
        
        title = None
        price = 0
        # mode 1
        root = tree.xpath("//div[@id='sc-list-goods']//ul[@class='clearfix']/li")
        if len(root) != 0:
            root = root[0]
            title = string.strip(root.xpath("//h2/a")[0].text)
            price = root.xpath("//div[@class='scrow-price']//em")[0].text
        elif len(tree.xpath("//div[@id='scList']//ul[@class='clearfix']/li")) != 0: # mode 2
            root = tree.xpath("//div[@id='scList']//ul[@class='clearfix']/li")[0]
            title = root.xpath("//h2/a")[0].attrib['title']
            price = root.xpath("//div[@class='scrow-price']//em")[0].text
        else:
            print 'result list is empty'
            h_file = codecs.open("%s.html" % datetime.datetime.now(), 'w', 'utf-8')
            h_file.write(u"%s" % source_html.decode('utf-8'))
            h_file.close()

        #print "title: %s - price: %s" % ( title, price)
        if price != None:
            price = float(price)
        return title, price

if __name__ == "__main__":
    import sys
    q_engine = HuiHui()
    t, p = q_engine.pquery(u"%s" % sys.argv[1].decode('utf-8'))
    #print t
    print p
