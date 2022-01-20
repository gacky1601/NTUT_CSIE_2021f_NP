# 04
# 輸入一組發票號碼
# 輸出對中當月哪一獎

from os import readlink
import  requests 
from  bs4  import  BeautifulSoup
import  csv
from  time  import  localtime,  strftime, time
from  os.path import  exists
import pandas as pd
def check(a,b):
    if(a==b[0]):
        print("中特別獎拉")
        return
    if(a==b[1]):
        print("中特獎拉")
        return
    for i in range(2,5):
        if(a==b[i]):
            print("中投獎拉")
            return
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
        print("中2獎拉")
        return
    if(max==6):
        print("中3獎拉")
        return
    if(max==5):
        print("中4獎拉")
        return
    if(max==4):
        print("中5獎拉")
        return
    if(max==3):
        print("中6獎拉")
        return
    if(a[-3:]==b[-1][-3:]):
        print("中加開6獎拉")
        return
    print("恭喜槓龜")
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
a=input()
check(a,num)