# -*- coding:utf-8 -*-

import urllib
from bs4 import BeautifulSoup
import os, time

#リンクを抽出する
html = open("eki-lik.html", encoding="utf-8").read()
soup = BeautifulSoup(html, "html.parser")
links = soup.select("a[href]")
result = []
for a in links:
	href = a.attrs["href"]
	title = a.string
	result.append((title, href))

#リンク先をダウンンロードする
savepath = "./out"
if not os.path.exists(savepath):
	os.mkdir(savepath)
for titlee, url in result:
	path = savepath + "/" + url + "html"
	#相対URLを絶対URLに変換
	a_url = urljoin("http://example.com", url)
	print("download = " + a_url)
	#ダウンロード
	urlretrieve(a_url, path)
	time.sleep(1)