# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import pandas as pd
import csv
import numpy as np
from matplotlib import pyplot as plt
from ggplot import *
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
movie_obj=pd.read_csv(r'C:\Users\aditya royal\Desktop\MLsoftaware_projects &datasets\movie_metadata.csv')

dictionary ={x:sum(movie_obj[x].isnull()) for x in movie_obj.columns if sum(movie_obj[x].isnull())!=0}
for x in movie_obj.columns:
   if isinstance(movie_obj[x],str)==False:
        movie_obj[x].fillna(0,inplace=True)

k=[]
for x in movie_obj.columns:
    if isinstance(movie_obj.ix[1,x],str):
        movie_obj.drop(x,axis=1,inplace=True)
#pd=pd.melt(movie_obj,id_vars=['duration'])
#p=ggplot(aes(x='duration',y='imdb_score'),data=movie_obj)+geom_line()
#print p
####################standardization#################################
x_std=StandardScaler()
y_trans=x_std.fit_transform(movie_obj.values)
y_trans=pd.DataFrame(y)
Column_names=list(movie_obj.columns)
y_trans.columns=Column_names
#y.iloc[:,0].plot()
correlation= y.corr()
ranked=correlation.rank(ascending=True)
k=correlation[(correlation<-0.4) | (correlation>0.4) & (correlation!=1)]
k.fillna(0,inplace=True)
k=k.ix[k.sum(axis=0)!=0,k.sum(axis=1)!=0]
#k[]
#y=pd.melt(y,id_vars=['duration'])
#print ggplot(aes(x='duration',y='value'),data=y)+geom_line()+facet_wrap('variable')
#########principal component analyss###
pca=PCA(n_components=9)
d=pca.fit_transform(y_trans)
####kmeans##########
k=KMeans(n_clusters=3)
y_clustered=k.fit_predict(y_trans)
match={0:'r',1:'b',2:'g'}
color=[match[l] for l in y_clustered]
plt.figure(figsize = (7,7))
plt.scatter(d[:,0],d[:,2],c=color,alpha=0.5)
plt.show()