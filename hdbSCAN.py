#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 23 14:49:47 2018

@author: cx513
"""

from sklearn.datasets import make_blobs
import pandas as pd

import hdbscan
import seaborn as sns
import matplotlib.pyplot as plt
import warnings

#tSNE100k=np.loadtxt("tSNE100k_default.out")

def hdbscanIntegration(data,min_cluster_size=15,min_samples=1,displayOnly=True):
    """
    Functions used to perform hdbscan on data
    See the documentation for explanation of parameters
    data is of form dim*num_points
    """
    #Computer may crash if min_cluster_size is too large
    if min_cluster_size>100:
        warnings.warn("Parameter min_cluster_size too large.",FutureWarning)
        directive=input("For continuing computation, press y:")
        if directive!='y':
            return 0
    #Generate the clusterer.
    clusterer=hdbscan.HDBSCAN(min_cluster_size,min_samples,prediction_data=True)
    #Feed the data into the clusterer
    clusterer.fit(data)
    #If the dimension of the data is greater than 2, return the clusterer
    if data.shape[1]>2:
        return clusterer
    #Or, we will plot a graph in python
    color_palette=sns.color_palette('deep',len(clusterer.labels_))
    #data samples that are not assigned to any cluster get -1,
    #and will be assigned color (0.5,0.5,0.5)
    cluster_colors = [color_palette[x] if x >= 0
                  else (0.5, 0.5, 0.5)
                  for x in clusterer.labels_]
    cluster_member_colors = [sns.desaturate(x, p) for x, p in
                         zip(cluster_colors, clusterer.probabilities_)]
    fig,ax=plt.subplots(figsize=(12,8))
    ax.scatter(*data.T, s=50, linewidth=0, c=cluster_member_colors, alpha=0.25)
    fig.show()
    if displayOnly==False:
        return clusterer,ax,fig

#clusterer = hdbscan.RobustSingleLinkage(cut=0.125, k=7)
#cluster_labels = clusterer.fit_predict(data)
#hierarchy = clusterer.cluster_hierarchy_
#alt_labels = hierarchy.get_clusters(0.100, 5)
#hierarchy.plot()

#clusterer = hdbscan.HDBSCAN(min_cluster_size=15).fit(data)
#blobs, labels = make_blobs(n_samples=2000, n_features=2)
    
    
    
    
#Things to Do:
#        tSNE 
#        clustering by hdbSCAN
#        using the labels to summarize
    