# 001.新北市公共自行車即時資訊
# url ='https://data.ntpc.gov.tw/api/datasets/71CD1490-A2DF-4198-BEF1-318479775E8A/csv/zip'
# (1)統計各站總停車格，
# 列出最多前五站，與停車格數量。
# (格式:sno sna tot)

# (2)統計各行政區有多少 UBIKE 站，
# 依序(由大到小)列出行政區，UBIKE 站數量
# (若數量相同則都要列出)

# 完成後舉手由助教檢查執行結果，上傳 Code。


import urllib.request  # 匯入套件
import zipfile
import csv
import pandas as pd

# 公開資料檔案
url = 'https://data.ntpc.gov.tw/api/datasets/71CD1490-A2DF-4198-BEF1-318479775E8A/csv/zip'
file_dir = 'Python/110/Test1/'  # 解壓縮目錄
zipName = 'F.zip'  # 壓縮檔案名稱
urllib.request.urlretrieve(url, zipName)  # 下載壓縮檔
f = zipfile.ZipFile(zipName)  # 開啟壓縮檔
for fileName in f.namelist():  # 壓縮檔案列表檔名
    f.extract(fileName, file_dir)  # 擷取壓縮檔案
f.close()  # 關檔
df = pd.read_csv(file_dir+fileName)
df = df.sort_values('tot', ascending=False)
print(df[['sno', 'sna', 'tot']].head(5))
df = df.groupby('sarea').count().sort_values('tot', ascending=False)
print(df['tot'])