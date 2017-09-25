from scipy import stats
import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt

# Getting the data from conver excel format
# !!!
# pdata Pandas data frame
# !!!
pdata = pd.read_csv('analysis.csv', delimiter=';')

# a = set()
rdata = pd.DataFrame(columns = [])
# pdata.__len__()

for i in range(0, 900000):
    try:
        rdata.set_value(pdata.iloc[i, 0], pdata.iloc[i, 6], pdata.iloc[i, 11])
    except:
        rdata.set_value(pdata.iloc[i, 0], pdata.iloc[i, 6], 0)


# print(rdata)


'''
rdata.set_value('id1', 'kol1', 'value1')
print(rdata)
rdata.set_value('id1', 'kol2', 'value2')

print(rdata)
'''
#


#  а тут должна быть обработка в новую pdata2, где в столбцах будут названия анализов а в строках показания одного человека на стррочку
# pdata['последний столбец'] = pd.Series(np.random.randn(932019), index=pdata.index)
CorrCoef = []

for i in range(0, len(rdata.columns)-1):
    for j in range (i+1, len(rdata.columns)):
        f = pd.DataFrame()
        f[i] = rdata.iloc[1:,i].copy()
        # print(f[i])
        f[j] = rdata.iloc[1:,j].copy()
        f = f.dropna(axis=0, how='any')
        if (not f.empty):

            # print(i, ' ', j)
            # print(f)
            print("korr")
            if (not f.corr.empty):
                print(f.corr())
                CorrCoef.append(f.corr())


        # print(f.corr())

# print(rdata)
'''
a = [[1,2,3],[2,4,6]]
b = [[1,2],[1,2],[5,3],[5,3],[7,9]]
adf = pd.DataFrame(a)
bdf = pd.DataFrame(b)
print(a)
print(b)
print(adf.corr())
print(bdf.corr())''' # а это значит что корреляция все же по столбцам
# for i in range(0, len(CorrCoef)):

    # CorrCoef[i] = CorrCoef.dropna(axis=0, how='any')
# for i in CorrCoef:
#     print(i)
#     print('\n')

