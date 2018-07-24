#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 15:07:39 2018

@author: cx513
"""

import plotly
plotly.tools.set_credentials_file(username='suzukaze',\
                                  api_key='tuJEp6bN9sRCxYMI9pVn')
import plotly.plotly as py
import plotly.graph_objs as go
import random
import numpy as np
import pandas as pd
from sklearn.datasets import make_blobs


def StratificationwithText(blobdata,label,Text):
    blobs, labels = make_blobs(n_samples=2000, n_features=2)
    blobs[labels==2]

def plotly2dDrawLabel():
#    plot the scatter points layer by laye
#    each layer contains the same label
    pass


l= []
y= []
data= pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/2014_usa_states.csv")
# Setting colors for plot.
N= 12
c= ['hsl('+str(h)+',50%'+',50%)' for h in np.linspace(0, 360, N)]
stanames=data['State']
preparedText=[]
for i in range(int(N)):
    preparedText.append([stanames[j]+str(i) for j in range(len(stanames))])
    
for i in range(int(N)):
    y.append((2000+i))
    trace0= go.Scatter(
        x= data['Rank'],
        y= data['Population']+(i*1000000),
        mode= 'markers',
        marker= dict(size= 14,
                    line= dict(width=1),
                    color= c[i],
                    opacity= 0.3
                   ),name= y[i],
        text= preparedText[i]
        ) # The hover text goes here... 
    l.append(trace0);

layout= go.Layout(
    title= 'Stats of USA States',
    hovermode= 'closest',
    xaxis= dict(
        title= 'Population',
        ticklen= 5,
        zeroline= False,
        gridwidth= 2,
    ),
    yaxis=dict(
        title= 'Rank',
        ticklen= 5,
        gridwidth= 2,
    ),
    showlegend= False
)
fig= go.Figure(data=l, layout=layout)
py.plot(fig)