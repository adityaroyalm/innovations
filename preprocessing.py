# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import pandas as pd
import csv
import numpy as np
from matplotlib import pyplot as ppl
from ggplot import *
movie_obj=pd.read_csv(r'C:\Users\aditya royal\Desktop\MLsoftaware_projects &datasets\movie_metadata.csv')

dictionary ={x:sum(movie_obj[x].isnull()) for x in movie_obj.columns if sum(movie_obj[x].isnull())!=0}
for x in movie_obj.columns:
   if isinstance(movie_obj[x],str)==False:
        movie_obj[x].fillna(0,inplace=True)

k=[]
for x in movie_obj.columns:
    if isinstance(movie_obj.ix[1,x],str):
        movie_obj.drop(x,axis=1,inplace=True)
pd=pd.melt(movie_obj,id_vars=['duration'])
p=ggplot(aes(x='duration',y='value'),data=pd)+geom_point()+facet_wrap('variable')
print p
