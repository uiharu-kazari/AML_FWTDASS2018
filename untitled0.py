#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 23 09:49:29 2018
Anti-Money Laudering
@author: cx513
"""

import pandas as pd

M1=pd.read_csv('M1.csv')
M2=pd.read_csv('M2.csv')
M3=pd.read_csv('M3.csv')
M4=pd.read_csv('M4.csv')
M5=pd.read_csv('M5.csv')
M6=pd.read_csv('M6.csv')

M=[M1,M2,M3,M4,M5,M6]

Months=['Feb','Mar','Apr','May','Jun','Jul']
for i in range(6):
    colname=list(map(str,range(1,9)))
    colname=['T'+colname[j]+Months[i] for j in range(8)]
    colname.insert(0,'Client ID')
    M[i].columns=colname

M=[M1,M2,M3,M4,M5,M6]

#Normalize the data ?

from functools import reduce

def dfInfiniteMerge(dflist,colname):
    """
    Merge dataframes in dflist, according to a common column name.
    """
    return reduce(lambda left,right:pd.merge(left,right,on=colname),dflist)

#Merge the data
Merged=dfInfiniteMerge(M,'Client ID')


import numpy as np
from sklearn.decomposition import PCA
from sklearn import preprocessing

X1=np.array(M1[M1.columns[1:]])
X1_normalized = preprocessing.normalize(X1, norm='l2')
X2=np.array(M1[M1.columns[1:]])
X2_normalized = preprocessing.normalize(X2, norm='l2')
X3=np.array(M1[M1.columns[1:]])
X3_normalized = preprocessing.normalize(X3, norm='l2')
X4=np.array(M1[M1.columns[1:]])
X4_normalized = preprocessing.normalize(X4, norm='l2')
X5=np.array(M1[M1.columns[1:]])
X5_normalized = preprocessing.normalize(X5, norm='l2')
X6=np.array(M1[M1.columns[1:]])
X6_normalized = preprocessing.normalize(X6, norm='l2')


XM=np.array(Merged[Merged.columns[1:]])
pca = PCA(n_components=2)
pca.fit(XM)

PCA(copy=True, iterated_power='auto', n_components=2, random_state=None,\
    svd_solver='auto', tol=0.0, whiten=False)
print(pca.explained_variance_ratio_)  

XM_normalized = preprocessing.normalize(XM, norm='l2')
pcaN=PCA(n_components=10)
pcaN.fit(XM_normalized)
PCA(copy=True, iterated_power='auto', n_components=10, random_state=None,\
    svd_solver='auto', tol=0.0, whiten=False)
print(pcaN.explained_variance_ratio_)  








