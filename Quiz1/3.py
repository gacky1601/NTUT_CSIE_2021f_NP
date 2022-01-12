# 003.
# 製作一個score.csv
# Name,English,Math,C,Python,Mid,Final
# John,90,70,90,60,50,80
# Tom,70,80,90,100,80,90
# Mary,80,90,70,90,100,90
# Ken,80,100,80,80,70,100
# Jack,60,70,50,90,60,100
# Lisa,70,90,80,80,90,80

# 用 pd 讀取 score.csv，變成 DataFrame
# 排序平均前三名，排序輸出名字與平均分數
# 列出C與Python平均分數 80以上的學生(Name, C, Python, 平均分數)

# 完成後舉手由助教檢查執行結果，上傳 Code。

import csv
import pandas as pd

df = pd.read_csv('score.csv')
df['Avg'] = df.mean(axis=1)
df = df.sort_values('Avg', ascending=False)
print(df[['Name', 'Avg']].head(3))
df['CPAvg'] = (df['C'] + df['Python']) / 2.0
print(df[df['CPAvg'] >= 80][['Name', 'C', 'Python', 'CPAvg']])
