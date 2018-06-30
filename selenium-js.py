# -*- coding:utf-8 -*-
from selenium import webdriver

#PhantomJSのドライバを得る
browser= webdriver.PhantomJS()
browser.implicitly_wait(3)

#適当なWebサイトを開く
browser.get("https://google.ci.jp")

r = browser.execute_script("return 100 + 50")
print(r)