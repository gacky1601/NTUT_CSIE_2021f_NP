# 004. 各國GDP資料
# https://storage.googleapis.com/learn_pd_like_tidyverse/gapminder.csv
# (1)統計lifeExp，
# 列出
# 全球lifeExp最老的國家與其相關資料。
# (country continent year lifeExp pop gdpPercap)
# (2)列出各洲(continent)在2007年，平均人均 GDP(gdpPercap)
# (如有多筆取平均)
# (格式:continent gdpPercap)
# (洲分為: Europe、Americas、Asia、Africa、Oceania)。

import csv
import pandas as pd

df = pd.read_csv('gapminder.csv')
df = df.sort_values('lifeExp', ascending=False)
print(df.head(1))
df = df[df['year'] == 2007]
print(df.groupby('continent')['gdpPercap'].mean())