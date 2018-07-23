#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 23 14:49:47 2018

@author: cx513
"""

from sklearn.datasets import make_blobs
import pandas as pd

blobs, labels = make_blobs(n_samples=2000, n_features=2)

pd.DataFrame(blobs).head()

import hdbscan
import seaborn as sns
import matplotlib.pyplot as plt

clusterer = hdbscan.HDBSCAN(min_cluster_size=15)

clusterer.fit(tSNE100k)

color_palette = sns.color_palette('deep', 1090)
cluster_colors = [color_palette[x] if x >= 0
                  else (0.5, 0.5, 0.5)
                  for x in clusterer.labels_]
cluster_member_colors = [sns.desaturate(x, p) for x, p in
                         zip(cluster_colors, clusterer.probabilities_)]
fig,ax=plt.subplots(figsize=(12,8))
ax.scatter(*tSNE100k.T, s=50, linewidth=0, c=cluster_member_colors, alpha=0.25)
fig.show()

def hbdscanIntegration():
    pass

#clusterer = hdbscan.RobustSingleLinkage(cut=0.125, k=7)
#cluster_labels = clusterer.fit_predict(data)
#hierarchy = clusterer.cluster_hierarchy_
#alt_labels = hierarchy.get_clusters(0.100, 5)
#hierarchy.plot()

#clusterer = hdbscan.HDBSCAN(min_cluster_size=15).fit(data)
