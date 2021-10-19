# 005
# 取得臺銀匯率資料
# https://rate.bot.com.tw/xrt?Lang=zh-TW
# 統計現金匯率:本行賣出，與即期匯率:本行賣出，
# 印出
# 兩者差距最大的前三種貨幣
# 並輸出取得的 年/月/日 時:分
# (格式: 現金匯率:本行賣出 即期匯率:本行賣出 幣別 抓取(牌告)時間)

import requests #匯入套件
from bs4 import BeautifulSoup #解析網頁
import csv #處理CSV檔案
from time import localtime, strftime #處理時間
from os.path import exists #台銀匯率網站
html = requests.get("https://rate.bot.com.tw/xrt?Lang=zh-TW") #回傳HTML檔案，轉存html物件
bsObj = BeautifulSoup(html.content, "lxml") #解析網頁，建立bs物件
a=0
b=0
c=0
maxa = 0
maxb = 0
maxc = 0
max2a = 0
max2b = 0
max2c = 0
namea = ""
nameb = ""
namec = ""
time = bsObj.find("span", {"class" : "time"}).string
for single_tr in bsObj.find("table", {"title":"牌告匯率"}).find("tbody").findAll("tr"): #針對匯率表格分析
    cell = single_tr.findAll("td") #找到每一個表格
    currency_name = cell[0].find("div", {"class":"visible-phone"}).contents[0] #找到表格中幣別
    currency_name = currency_name.replace("\r","") #取代不需要的字元
    currency_name = currency_name.replace("\n","")
    currency_name = currency_name.replace(" ","")
    currency_rate = cell[2].contents[0] #找到幣別匯率
    currency_rate1 = cell[4].contents[0]
    currency_rate1 = currency_rate1.replace("\r","")
    currency_rate1 = currency_rate1.replace("\n","")
    currency_rate1 = currency_rate1.replace(" ","")
    try:
        if (float(currency_rate)-float(currency_rate1)) > a:
            namea = currency_name
            a=float(currency_rate)-float(currency_rate1)
            maxa = float(currency_rate)
            max2a = float(currency_rate1)
    except:
        pass
    try:
        if a>(float(currency_rate)-float(currency_rate1)) > b:
            nameb = currency_name
            b=float(currency_rate)-float(currency_rate1)
            maxb = float(currency_rate)
            max2b = float(currency_rate1)
    except:
        pass
    try:
        if b>(float(currency_rate)-float(currency_rate1)) > c:
            namec = currency_name
            c=float(currency_rate)-float(currency_rate1)
            maxc = float(currency_rate)
            max2c = float(currency_rate1)
    except:
        pass
    

print(namea,maxa,max2a,time)
print(nameb,maxb,max2b,time)
print(namec,maxc,max2c,time)