# 04
# 輸入全班五位同學的英文名字
# 隨機產生 programming Language, Math, English 三科成績 (0~100分)
# 每一科成績建置一個 series
# 三科成績資料建置出 DataFrame
# 輸出各科最高成績分數和名字
# 輸出全班各科平均、中位數

import pandas as pd
population_dict = {'California': 39250017, 'Texas': 27862596,
'Florida': 20612439, 'New York': 19745289,
'Illinois': 12801539}
area_dict = {'California': 423967, 'Texas': 695662,
'New York': 141297, 'Florida': 170312, 'Illinois': 149995}
#建構二個Series
population = pd.Series(population_dict)
area = pd.Series(area_dict)
# DataFrame是一維的 Series
states = pd.DataFrame({'population': population,
'area': area})
print(states)
#DataFrame有index屬性存取索引，columns屬性
print(states.index)
print(states.columns)