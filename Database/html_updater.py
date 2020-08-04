"""
各ポケモンの種族値を得るHTMLデータを更新する。
ポケマピ(https://pokemongo-get.com/status-ranking/)のHTMLを取得し保存するスクリプト

"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import codecs

urlName = "https://pokemongo-get.com/status-ranking/"

options = Options()

options.set_headless(True)

driver = webdriver.Chrome(r"C:\Users\ktmks\programming\chromedriver_win32\chromedriver.exe",chrome_options=options)

driver.get(urlName)

html = driver.page_source.encode("utf-8")

f = codecs.open(r"C:\Users\ktmks\programming\GUI_app\Data\pokemapi.html","w","utf-8")
f.write(html.decode('utf-8'))
f.close()


