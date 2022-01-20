# 03
# 輸出
# 台北市、新北市
# 哪一條街、或路，7-11店數最多

# %%
import requests
import pandas as pd
city = ['台北市', '新北市']

roadAddressRecord ={}
roadAddressRecord1 ={}
for index, city in enumerate(city):
    data = {'strTargetField':'COUNTY','strKeyWords':'%s' % city}
    res = requests.post('https://www.ibon.com.tw/retail_inquiry_ajax.aspx', data=data)
    count = pd.read_html(res.text, header=0)[0].shape[0]
    data = pd.read_html(res.text, header=0)[0]
    for i in range(count-1):
        fullAddress = data.iloc[i,2]
        start = fullAddress.find(city[0])
        end = fullAddress.find('路')+1
        if end<9: continue
        roadAddress = fullAddress[start:end]
        if roadAddress not in roadAddressRecord:
            roadAddressRecord[roadAddress]=1
        else:
            roadAddressRecord[roadAddress]+=1
    

    for i in range(count):
        fullAddress1 = data.iloc[i,2]
        start1 = fullAddress1.find(city[0])
        end1 = fullAddress.find('街')+1
        if end1<9: continue
        roadAddress1 = fullAddress[start1:end1]
        if roadAddress1 not in roadAddressRecord:
            roadAddressRecord[roadAddress1]=1
        else:
            roadAddressRecord[roadAddress1]+=1
            print(roadAddress1)

print('------最多小七的路、街名---------')
num=0

for key, value in sorted(roadAddressRecord.items(), key=lambda item:item[1], reverse=True):
    if (num>=3): break
    print(key[6:], ',', value,',',key[0:3])
    num = num +1 

# %%
