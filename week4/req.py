import pandas
import requests
from bs4 import BeautifulSoup as bs
browser={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36"}
res=requests.get('https://rate.bot.com.tw/ir?Lang=zh-TW&redirect=true',headers=browser)
dd=pandas.read_html('https://rate.bot.com.tw/xrt?Lang=zh-TW')
currency=dd[0]
print(currency)
CNY_TW=currency.iloc[18,2]
float(CNY_TW)
doc={
    'CNY': CNY_TW
}
print(doc)

def date_num(dt):
    try:
        c=dt.split('/')
        x=c[0]+c[1]+c[2]
        return int(x)
    except:
        pass