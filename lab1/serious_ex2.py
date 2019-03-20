from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel
from collections import OrderedDict

url = "http://s.cafef.vn/bao-cao-tai-chinh/VNM/IncSta/2017/3/0/0/ket-qua-hoat-dong-kinh-doanh-cong-ty-co-phan-sua-viet-nam.chn"
conn = urlopen(url)
raw_data = conn.read()
html_content = raw_data.decode("utf-8")

with open("baocaotaichinh.html", "wb") as f:
    f.write(raw_data)

soup = BeautifulSoup(html_content, "html.parser")
table = soup.find("table", id="tableContent")
row_content = table.find_all("tr")
news_content=[]
for tr in row_content:
    title = tr.td
    print(title)
    