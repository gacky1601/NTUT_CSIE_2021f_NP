# 輸出目前
# 現金買入
# 即期賣出
# 匯率最高的幣別與匯率、抓取(牌告)時間

import requests #匯入套件
from bs4 import BeautifulSoup #解析網頁
import csv #處理CSV檔案
from time import localtime, strftime #處理時間
from os.path import exists #台銀匯率網站
html = requests.get("https://rate.bot.com.tw/xrt?Lang=zh-TW") #回傳HTML檔案，轉存html物件
bsObj = BeautifulSoup(html.content, "lxml") #解析網頁，建立bs物件
a=0
max = 0
namea = ""

time = bsObj.find("span", {"class" : "time"}).string
for single_tr in bsObj.find("table", {"title":"牌告匯率"}).find("tbody").findAll("tr"): #針對匯率表格分析
    cell = single_tr.findAll("td") #找到每一個表格
    currency_name = cell[0].find("div", {"class":"visible-phone"}).contents[0] #找到表格中幣別
    currency_name = currency_name.replace("\r","") #取代不需要的字元
    currency_name = currency_name.replace("\n","")
    currency_name = currency_name.replace(" ","")
    currency_rate = cell[1].contents[0] #找到幣別匯率
    currency_rate1 = cell[3].contents[0]
    currency_rate1 = currency_rate1.replace("\r","")
    currency_rate1 = currency_rate1.replace("\n","")
    currency_rate1 = currency_rate1.replace(" ","")
    try:
        if float(currency_rate) > max:
            namea = currency_name
            max=float(currency_rate)
    except:
        pass
 

print(namea,currency_rate,currency_rate1,time)
