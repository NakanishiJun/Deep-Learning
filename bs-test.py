# -*- coding:utf-8 -*-
from bs4 import BeautifulSoup

html = """
<html><body>
  <h1>スクレイピング</h1>
  <p>Webページを解析すること</p>
  <p>任意の箇所を抽出すること</p>
 </body></html>
 """

 soup = BeautifulSoup(html, 'html.paeser')

 h1 = soup.html.body.h1
 pi = soup.html.body.p
 p2 = p1 .next_sibling.next_sibling


 print("h1 = " + h1.string)
 print("p = " + p1.string)
 print("p = " + p2.string)