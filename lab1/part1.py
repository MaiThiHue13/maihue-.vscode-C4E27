from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel
from collections import OrderedDict


url = "https://www.apple.com/itunes/charts/songs"
conn= urlopen(url)

raw_data=conn.read()
html_content = raw_data.decode('utf-8')

soup= BeautifulSoup(html_content, "html.parser")
section =soup.find("section", "section chart-grid")
li_list = section.div.ul.find_all("li")

news_list=[]
for li in li_list:
    a=li.h3.a
    title = a.string
    link =url + a["href"]
    news = OrderedDict({
        "title":title.lstrip().rstrip(),
        "link":link
    })

    news_list.append(news)

pyexcel.save_as(records=news_list, dest_file_name="itunetopsong.xlsx")