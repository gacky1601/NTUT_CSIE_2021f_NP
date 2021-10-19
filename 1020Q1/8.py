# 008.
# 利用財政部統一發票兌獎網頁(https://invoice.etax.nat.gov.tw/)，
# 對最新一期的發票，
# 輸入 N
# 再輸入 N 張統一發票號碼，
# 輸出哪一張對中哪一個獎，多少錢(若無中獎則輸出0)
# 並加總所有獎金，以及平均一張獲得多少獎金

from os import readlink
import  requests 
from  bs4  import  BeautifulSoup
import  csv
from  time  import  localtime,  strftime, time
from  os.path import  exists
import pandas as pd
def check(a,b):
    if(a==b[0]):
        print("中特別獎 獎金：10000000")
        return 10000000
    if(a==b[1]):
        print("中特獎 獎金：2000000")
        return 2000000
    for i in range(2,5):
        if(a==b[i]):
            print("中頭獎 獎金：2000000")
            return 200000
    max=0
    for i in b[2:5]:
        iqw=0
        for j in range(8):
            if(i[7-j]==a[7-j]):
                iqw+=1
            else:
                break
        if(max<iqw):
            max=iqw
    if(max==7):
        print("中2獎 獎金：40000")
        return 40000
    if(max==6):
        print("中3獎 獎金：10000")
        return 10000
    if(max==5):
        print("中4獎 獎金：4000")
        return 4000
    if(max==4):
        print("中5獎 獎金：1000")
        return 1000
    if(max==3):
        print("中6獎 獎金：200")
        return 200
    if(a[-3:]==b[-1][-3:]):
        print("中加開6獎 獎金：200")
        return 200
    print("恭喜槓龜")
    return 0
num=[]
html =  requests.get("https://invoice.etax.nat.gov.tw") 
bsObj =  BeautifulSoup(html.content,"html.parser")
for  single_tr in  bsObj.find("table",  {"summary":"統一發票中獎號碼"}).findAll("tr"):
    cell = single_tr.findAll("td") #找到每一個表格
    try:
        num.append(cell[1].find("span", {"class":"t18Red"}).contents[0])
    except:
        pass
new=num[2].split("、")
num=num[:2]+new+num[3:]
#qw=pd.DataFrame({'ci':pd.Series(ci),'co':pd.Series(co),'i':pd.Series(i),'o':pd.Series(o)})
x=int(input())
g=0
for i in range(0,x):
    a=input()
    g+=check(a,num)
print('獎金總額',g)
print('每張平均中：',int(g/x))