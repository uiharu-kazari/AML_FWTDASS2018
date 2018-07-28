#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 25 10:26:07 2018

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

def NarrtoStr(array):
        return str(round(array[0]))+\
                ','+str(round(array[1]))+\
                ','+str(round(array[2]))


def irokaiden(ColorList):
    npa=np.array(ColorList)
    npa=npa*255
    result=[]
    for i in range(len(npa)):
#        print(npa[i])
        temp='rgb('+NarrtoStr(npa[i])+')'
        result.append(temp)
    return result
    

trace1 = go.Scatter(
    y = np.random.randn(500),
    mode='markers',
    marker=dict(
        size=16,
        color = irokaiden(cluster_member_colors), #set color equal to a variable
#        colorscale='Viridis',
        showscale=True
    )
)
data = [trace1]

py.plot(data)