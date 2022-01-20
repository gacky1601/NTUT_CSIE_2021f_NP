# 參考 page 21
# 製作 XML menu 檔案
# 讀取檔案，輸出早餐、午餐、晚餐相關資料
# breakfast
# hours: 7-11
# breakfast burritos, price: $60
# pancakes, price $40
# ...
# ....
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

