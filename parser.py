__author__ = 'rt3lpiz'

from bs4 import BeautifulSoup
import urllib2

url='http://dimeshop.ru/product/baofeng-uv-b5-5w-99ch-uhfvhf-a1011a-1sht/?msg=ofxe#product-request'
data=urllib2.urlopen(url)
soup=BeautifulSoup(data,'html5lib')
# print soup.prettify()
for title in soup.find_all(True):
    print title.get_text()