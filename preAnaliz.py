from scipy import stats
import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt
from scipy.stats.stats import pearsonr
import scipy as sc

# Getting the data from conver excel format
# !!!
# pdata Pandas data frame
# !!!
pdata = pd.read_csv('analysis.csv', sep = ';', delimiter = ';')

a = set()
rdata = pd.DataFrame(columns = [])
# pdata.__len__()

for i in range(0, 90000):
    try:
        rdata.set_value(pdata.iloc[i, 0], pdata.iloc[i, 6], float(pdata.iloc[i, 9]))
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
        f[j] = rdata.iloc[1:,j].copy()
        f = f.dropna(axis=0, how='any')


        if (not f.empty):

            # print(i, ' ', j)
            # print(f)

            a = np.array(f[i],float)
            b = np.array(f[j],float)
            # print(b)
            print("korr")
            print(pearsonr(a, b))
            # print(f)

            # print('ALERT' ,i, ' ', j, ' ', f[i],' ', f[j])



            CorrCoef.append(pearsonr(f[i], f[j]))
        # a = sc.array(rdata.iloc[1:,i])
        # b = sc.array(rdata.iloc[1:,j])
        # print(a)
        # print(pearsonr(a, b))

        # print(f.corr())

# print(rdata)

# a = [[1,2,3],[2,4,6]]
# b = [[1,2],[1,2],[5,3],[5,3],[7,9]]
# adf = pd.DataFrame(a)
# bdf = pd.DataFrame(b)
# # print(a)
# # print(b)
# # print(adf.corr())
# print(type(b))
# ca = sc.array(b[:][0].copy())
# cb = sc.array(b[1][:])
# print(b[:][2])
# r_row, p_value = pearsonr(ca,cb)
# print(pearsonr(ca,cb))  # а это значит что корреляция все же по столбцам
# а потом пошла дикая дичь с попыткой выработать корр функцию
# for i in range(0, len(CorrCoef)):

    # CorrCoef[i] = CorrCoef.dropna(axis=0, how='any')
# for i in CorrCoef:
#     print(i)
#     print('\n')



