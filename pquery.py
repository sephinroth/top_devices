import urllib2
from lxml import etree

class HuiHui:
    def __init__(self):
        self.url = 'http://www.huihui.cn/search?q='

    def pquery(self, keywords):
        qstring = self.url + "+".join(keywords)
        content = urllib2.urlopen(qstring.encode('utf-8'))

        tree = etree.HTML(content.read())
        if len(tree.xpath("//div[@id='scRecommend']/div/div[@class='noresult']")) != 0:
            return None, None

        root = tree.xpath("//div[@id='scList']//ul[@class='clearfix']/li")
        if len(root) == 0:
            return None, None
        else:
            root = root[0]
        title = root.xpath("//h2/a")[0].attrib['title']
        price = root.xpath("//div[@class='scrow-price']//em")[0].text
        return price, title

