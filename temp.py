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
pdata = pd.read_csv('analysis.csv', sep = ';')
rdata = pd.read_csv('analysis.csv', sep = ';', delimiter = ';')
print (pdata)
print(rdata == pdata)