#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 23 11:06:45 2018

@author: cx513
"""


from sklearn.manifold import TSNE

import matplotlib.pyplot as plt

#tsnetrail=TSNE(n_components=2).fit_transform(X_normalized[:100000])

#x=tsnetrail[:,0]
#y=tsnetrail[:,1]

#fig,ax=plt.subplots(figsize=(12,8))
#colors = np.random.rand(len(x))
#ax.scatter(x,y,alpha=0.6,c=colors)
#fig.show()

def tSNE(array,n_components=2,displayOnly=True):
    """
    t-SNE and plot.
    Use default values.
    Plotting to be updated, sync with plotly
    """
    tsneA=TSNE(n_components).fit_transform(array)
    x=tsneA[:,0]
    y=tsneA[:,1]
    fig,ax=plt.subplots(figsize=(12,8))
    colors = np.random.rand(len(x))
    ax.scatter(x,y,alpha=0.6,c=colors)
    fig.show()
    if displayOnly==False:
        return tsneA,fig

def fancySP(x,y):
    fig,ax=plt.subplots(figsize=(12,8))
    colors = np.random.rand(len(x))
    ax.scatter(x,y,alpha=0.6,c=colors)
    fig.show()
    












