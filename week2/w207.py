# page 17 menu
# 製作Json 檔案，讀入 轉成(load) Python 資料型別 印出
# (參考 page 19)

import json
with open("example.json",encoding = 'utf8') as file:
    data = json.load(file)
for item in data:
    print(item)
