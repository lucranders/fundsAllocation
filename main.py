import pandas as pd
import buildDf as bd
from scipy.optimize import linprog
import numpy as np

fiiDf = pd.read_csv('ListFiis.txt' , header = None)
tolValues = pd.read_csv('tolValues.txt' , header = None)
fiiDf.columns = ['FII','Part']
tolValues.columns = ['pvp','invest']
fiiDf.loc[:,'FII'] = fiiDf.FII.str.lower()

mainInfos = bd.gather_(fiiDf.FII)
mainInfos.columns = ['FII','pvp','value','dy']
totalDf = mainInfos.merge(fiiDf,on = ['FII'],how = 'inner')

columns_ = []
b = []
for pt_ in totalDf.Part.unique():
    totalDf.loc[:,'Pt'+str(pt_)] = totalDf.Part.apply(lambda x: -1 if x == pt_ else 0)
    columns_.append('Pt'+str(pt_))
    b.append(-1)

totalDf.loc[:,'PvpTot'] = totalDf.pvp - tolValues.pvp.values
columns_.append('PvpTot')
b.append(0)
columns_.append('value')
b.append(tolValues.invest.values[0])
A = totalDf[columns_].values.transpose()
c = -totalDf.dy.values*totalDf.value.values
answ = linprog(c = c, A_ub=A, b_ub=b)
if answ.success:
    totalDf.loc[:,'Qt'] = np.round(answ.x,0)
totalDf.loc[:,'expectedIncome12M'] = np.round(-totalDf.Qt * c/100,2)
printCols = [x for x in totalDf.columns if 'Pt' not in x and 'PvpTot' not in x]
print(totalDf[printCols])
print('Cost: ' + str(np.sum(totalDf.loc[:,'Qt']*totalDf.loc[:,'value'])))
print('Expected income (12M): ' + str(np.round(np.sum(totalDf.loc[:,'expectedIncome12M']),2)))

