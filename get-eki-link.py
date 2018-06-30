# -*- coding:utf-8 -*-
from bs4 import BeautifulSoup

#解析対象となるHTMLを読み込む
html = open("eki-link.html", encoding = "utf-8").read()

#HTML解析
soup = BeautifulSoup(html, "html.parser")

#aタグの取得
links = soup.select("a[href]")

#(タイトル、URL)のリストを作成
result = []
for a in links:
	href = a.attrs["href"]
	title = a.string
	result.append((title, href))

print(result)