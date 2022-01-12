import pandas
import requests
from bs4 import BeautifulSoup as bs
from pprint import pprint
import time
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import time
date=time.strftime("%Y-%m-%d", time.localtime())
def find(current_type):
    type=""
    for i in range(len(current_type)-1,0,-1):
        if current_type[i] ==")":
            continue
        if current_type[i]== "(":
            type=type[::-1]
            break
        type=type+current_type[i]
    return type

# 引用私密金鑰
# path/to/serviceAccount.json 請用自己存放的路徑
cred = credentials.Certificate('pyradise-b6393-firebase-adminsdk-ybuy4-a0c0143bc1.json')
# 初始化firebase，注意不能重複初始化
firebase_admin.initialize_app(cred)
# 初始化firestore
db = firestore.client()

def getdata():

    browser={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36"}
    res=requests.get('https://rate.bot.com.tw/ir?Lang=zh-TW&redirect=true',headers=browser)
    dd=pandas.read_html('https://rate.bot.com.tw/xrt?Lang=zh-TW')
    currency=dd[0]
    doc={}
    for j in range(0,19):
        current_type=currency.iloc[j,0]
        current_rate=currency.iloc[j,2]
        type=find(current_type)
        if current_rate=='-':current_rate=0
        doc[type]=float(current_rate)
        # print(type," ",current_rate)
        # print("<item>",type,"</item>")
    m=str(int(time.time()))
    doc_ref=db.collection("exchange_rate").document(m).set(doc)
    print("Success")


getdata()