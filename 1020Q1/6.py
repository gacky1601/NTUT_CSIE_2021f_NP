# 006.
# 使用[臺灣證交所本國上市證券網站]。
# http://isin.twse.com.tw/isin/C_public.jsp?strMode=2
# 統計"臺灣證交所本國上市證券" 各股票的上市日期
# 列出
# 上市時間最久的前十名 與其股票名稱 與產業別
# (格式: 股票 上市日 產業別)

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
del newdf['有價證券代號及名稱'], newdf['市場別'], newdf['國際證券辨識號碼(ISIN Code)'],newdf['股票名稱']
print(newdf)

a=newdf.sort_values('上市日')
print(a.head(10))