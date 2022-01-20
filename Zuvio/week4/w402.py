# 本國上市證券國際證券辨識號碼一覽表

# 1.抓取輸出
# 股票編號、股票名稱、產業別
# 2.輸出
# 最多上市公司產業別、數量

# %%
from datetime import datetime
import pandas as pd

df = pd.read_html('http://isin.twse.com.tw/isin/C_public.jsp?strMode=2',encoding='big5hkscs', header=0)
newdf = df[0][df[0]['產業別'] > '0']
del newdf['CFICode'], newdf['備註']
df2 = newdf['有價證券代號及名稱'].str.split(' ', expand=True)
df2 = df2.reset_index(drop=True)
newdf = newdf.reset_index(drop=True)
for i in df2.index:
    if ' ' in df2.iat[i, 0]:
        df2.iat[i, 1] = df2.iat[i, 0].split(' ')[1]
        df2.iat[i, 0] = df2.iat[i, 0].split(' ')[0]
newdf = df2.join(newdf)
newdf = newdf.rename(columns={0: '股票代號', 1: '股票名稱'})
del newdf['有價證券代號及名稱'], newdf['市場別'], newdf['國際證券辨識號碼(ISIN Code)'],newdf['股票名稱'],newdf['上市日']
print(newdf)

a=newdf.sort_values('產業別')
x=a.groupby('產業別').describe()
y=x.sort_values(('股票代號',  'count'),ascending=False)
print(y.head(1)[('股票代號',  'count')])
# %%