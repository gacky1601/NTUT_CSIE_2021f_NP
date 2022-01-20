# 005
# 製作一個score.csv
# Name, quiz1, quiz2, quiz3, quiz4, mid, final
# John, 90, 70, 90, 60, 50, 80
# Tom, 70, 80, 90, 100, 80, 90
# Mary, 80, 90, 70, 90, 100, 90
# Ken, 80, 100, 80, 80, 70, 100

# 用 pd 讀取 score.csv，變成 DataFrame
# 排序平均前三名，排序輸出名字與平均分數
# 列出平均分數大於 85 的資料
# 列出各科最高與最低分與其名字

import csv


def build_level2_dict(source_file):
    new_dict = {}
    with open(source_file, 'rb')as csv_file:
        data = csv.DictReader(csv_file, delimiter=",")
    for row in data:
        item = new_dict.get(row['country'], dict())
        item[row['name']] = {k: row[k] for k in ('id','age')}
        new_dict[row['country']] = item
    return new_dict


import pandas as pd
import numpy as np

data = build_level2_dict('score.csv')
df = pd.DataFrame(data, columns=['Name']
)
# 設定索引名稱
df.index.name = 'id'
print(df)