#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 14:26:32 2018

@author: cx513
"""

import plotly
plotly.tools.set_credentials_file(username='suzukaze',\
                                  api_key='tuJEp6bN9sRCxYMI9pVn')
import plotly.plotly as py
import plotly.graph_objs as go
import warnings
import random
import numpy as np

#class DimensionIncompatibleWarning(UserWarning):
#    pass

class DimensionError(Exception):
    pass


def plotly3dDraw(colorarray,*args):
    """
    Insert zero if no color assigned
    colorarray should be of the same length as x (or y or z)
    """
    if len(args)==3:
        (x,y,z)=args
    elif len(args)==1:
        #Notice that using *args then args is of type list
        inputmatrix=np.array(args[0])
        (x,y,z)=(inputmatrix[:,0],inputmatrix[:,1],inputmatrix[:,2])
    else:
        #warnings.warn("Incompatible dimension",DimensionIncompatibleWarning)
        raise DimensionError('Input\'s dimension Incompatible.')
    colorarray=[x,y,z][np.random.randint(0,3)]
    preparedline=dict(color='rgba(217, 217, 217, 0.14)',width=0.5)
    preparedText=list(map(str,np.random.randint(1,20,len(x))))
    trace= go.Scatter3d(\
        x=x,\
        y=y,\
        z=z,\
        mode='markers',\
        text=preparedText,\
        marker=dict(size=2,color=colorarray,\
                    colorscale='Viridis',line=preparedline,opacity=0.8)\
        )
    data=[trace]
    layout = go.Layout(margin=dict(l=0,r=0,b=0,t=0))
    fig = go.Figure(data=data, layout=layout)
    output=py.plot(fig, filename='simple-3d-scatter',auto_open=False)
    return output

#random.sample(range(10),4)
#DN1=tSNE(X1_normalized[:2000],False,n_components=3)
#DN1=tSNE(X1_normalized[random.sample(range(100000),4000)],False,n_components=3)
    
