# -*- coding:utf-8 -*-
#BeautifulSoupを利用してHTMLを解析
import BeautifulSoup
import io
html = io.open("eki-link.html", encoding="utf-8").read()
soup = BeautifulSoup(html, "html.parser")

#テーブルを解析
result = []

#tableタグを得る
table = soup.select_one("table")

#trタグを得る
tr_list = table.find_all("tr")
for tr in tr_list:
	result_row = []
	td_list = tr.find_all(["td", "th"])
	for td in td_list:
		cell = td.get_text()
		result_row.append(cell)
	result.append(result_row)

#リストをCSVファイルとして出力
for row in result:
	print(",".join(row))