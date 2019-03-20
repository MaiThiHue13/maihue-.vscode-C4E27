from urllib.request import urlopen
from bs4 import BeautifulSoup
from youtube_dl import YoutubeDL

url = "https://www.apple.com/itunes/charts/songs"
conn = urlopen(url)
raw_data = conn.read()

html_content = raw_data.decode("utf8")
soup =BeautifulSoup(html_content,"html.parser")
div = soup.find("div",id="main")
li_list = div.find_all("li")

item_list = []
for li in li_list:
    a = li.h3.a
    title = a.string
    item_list.append(title)
#print(item_list)

option={
    'outtmpl': '/download/%(title)s.%(ext)s',
    'default_search':'ytsearch',
    'max_downloads':1 
}

dl = YoutubeDL(option)
dl.download(item_list)