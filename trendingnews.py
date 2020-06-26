
# Author : DIVS TECH

import bs4
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen
newsurl="https://news.google.com/news/rss"
root=urlopen(newsurl)
xmlpage=root.read()
root.close()
souppage=soup(xmlpage,"xml")
newslist=souppage.findAll("item")
for news in newslist:
	print(news.title.text)
	print(news.pubDate.text)
	print("-\n"*60)