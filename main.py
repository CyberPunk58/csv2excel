import pandas as pd
import os
from openpyxl import Workbook

df1 = pd.DataFrame()

fileCSV = os.listdir("D:\\Pavel\\Data\\nstats_032023")
filesCSV = [os.path.join("D:\\Pavel\\Data\\nstats_032023", file) for file in fileCSV]
filesCSVsorted = sorted(filesCSV, key = os.path.getmtime) #Сортируем по дате создания файла для нужного порядка в итоговом файле
for file in range(0, len(filesCSVsorted)):
    df2 = pd.read_csv(filesCSVsorted[file], sep=',')
    df2 = df2.drop(columns='day')
    df1 = pd.concat((df1,df2),axis = 1)

df1.to_excel("D:\\Pavel\\Data\\nstats_032023_total\\"+"total"+".xlsx", index=False)


df = pd.read_excel("D:\\Pavel\\Data\\nstats_032023_total\\total.xlsx")
df['row_sum'] = df.sum (axis=1)
df.to_excel("D:\\Pavel\\Data\\nstats_032023_total\\"+"total_with_sum"+".xlsx", index=False)


