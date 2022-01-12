# 007.
# 針對 7-eleven各門市資訊，利用 ibon 網頁(https://www.ibon.com.tw/retail_inquiry_ajax.aspx)
# 分別統計小七所在的街名、路名，
# 列出最多小七的街名、和路名的各前三名與數量，
# 以及其所在的縣市。

# %%
import requests
import pandas as pd
city = ['基隆市', '台北市', '新北市', '桃園市', '新竹市','新竹縣','苗栗縣','台中市','彰化縣', '雲林縣', '南投縣', '嘉義縣', '嘉義市', '台南市', '高雄市', '屏東縣', '台東縣', '花蓮縣', '宜蘭縣', '連江縣', '金門縣', '澎湖縣']

roadAddressRecord ={}
roadAddressRecord1 ={}
for index, city in enumerate(city):
    data = {'strTargetField':'COUNTY','strKeyWords':'%s' % city}
    res = requests.post('https://www.ibon.com.tw/retail_inquiry_ajax.aspx', data=data)
    count = pd.read_html(res.text, header=0)[0].shape[0]
    data = pd.read_html(res.text, header=0)[0]
    for i in range(count):
        fullAddress = data.iloc[i,2]
        start = fullAddress.find(city[0])
        end = fullAddress.find('路')+1
        if end<9: continue
        roadAddress = fullAddress[start:end]
        if roadAddress not in roadAddressRecord:
            roadAddressRecord[roadAddress]=1
        else:
            roadAddressRecord[roadAddress]+=1
    
        # start1 = fullAddress.find(city[0])
        # end1 = fullAddress.find('街')+1
        # if end1<8: continue
        # roadAddress1 = fullAddress[start1:end1]
        # if roadAddress1 not in roadAddressRecord1:
        #     roadAddressRecord1[roadAddress1]=1
        # else:
        #     roadAddressRecord1[roadAddress1]+=1

    for i in range(count):
        fullAddress = data.iloc[i,2]
        start1 = fullAddress.find(city[0])
        end1 = fullAddress.find('街')+1
        if end1<9: continue
        roadAddress1 = fullAddress[start1:end1]
        if roadAddress1 not in roadAddressRecord1:
            roadAddressRecord1[roadAddress1]=1
        else:
            roadAddressRecord1[roadAddress1]+=1

print('------最多小七的路名前3名---------')
num=0
for key, value in sorted(roadAddressRecord.items(), key=lambda item:item[1], reverse=True):
    if (num>=3): break
    print(key[6:], ',', value,',',key[0:3])
    num = num +1 

print('------最多小七的街名前3名---------')
num=0
for key, value in sorted(roadAddressRecord1.items(), key=lambda item:item[1], reverse=True):
    if (num>=3): break
    if(key==''):
        pass
    else:
        print(key[6:], ',', value,',',key[0:3])
        num = num +1 
# %%
