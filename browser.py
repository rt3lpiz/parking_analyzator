__author__ = 'rt3lpiz'

import mechanize
from bs4 import BeautifulSoup

br=mechanize.Browser()
pagina=br.open("http://seedchan.net/")
data=pagina.read()
soup=BeautifulSoup(data)
for element in soup.find_all('td', class_="ranking-sub"):
    print element.get_text()
