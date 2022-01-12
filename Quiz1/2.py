# 002.
# 參考 page 25，製作 country_data.xml 檔案
# 讀取檔案，輸出country name、rank、year、gdppc、neighbor name相關資料
# country name:
# rank:
# year:
# gdppc:
# neighbor name

# 完成後舉手由助教檢查執行結果，上傳 Code。

import xml.etree.ElementTree as et
tree = et.ElementTree(file='country_data.xml') 
i=0
b=""
root = tree.getroot()
for child  in root : 
    
    print( child.tag, ':', child.attrib['name'])
    print("rank:"+root[i][0].text)
    print("year:"+root[i][1].text)
    print("gdppc:"+root[i][2].text)
    for neighbor in root[i][3].iter('neighbor'):
        b=b+" "+neighbor.attrib["name"]
    print("neighbor name:"+b)
    
    i+=1

