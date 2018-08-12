# -*- coding:utf-8 -*- 

import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

#ユーザ名とパスワードの指定

USER = "JS-TESTER"
PASS = "ipCU12ySxI"

#セッションの開始
session = requests.session()

login_info = {
	"username_mmlbbs6" : USER,
	"password_mmlbbs6" : PASS,
	"back" : "index.php",
	"mml_id" : "0"
}

url_login = "https://uta.pw/sakusibbs/users.php?action=login&m=try"
res = session.post(url_login, data=login_info)
res.raise_for_status() #エラーならここで例外を発生させる

#マイページのURLをピックアップさせる
soup = BeautifulSoup(res.text, "html.parser")
a = soup.select_one(".islogin a")
if a is None:
	print("マイページが取得できませんでした")
	quit()
#相対URLを絶対URLに変換
url_mypage = urljoin(url_login, a.attrs["href"])
print("マイページ = ", url_mypage)

#マイページにアクセス
res = session.get(url_mypage)
res.raise_for_status()

#お気に入りの詞のタイトルを列挙
soup = BeautifulSoup(res.text, "html.parser")
links = soup.select("#favlist li > a")
for a in links:
	href = a.attrs["href"]
	title = a.get_text()
	print("-", title, ">". href)
