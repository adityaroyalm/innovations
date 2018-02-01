# -*- coding: utf-8 -*-
"""
Created on Sun Mar 05 09:10:47 2017

@author: aditya royal
"""

import pandas as pd
import ggplot as gg
import numpy as np
movie=pd.read_csv('C:/Users/aditya royal/Desktop/MLsoftaware_projects/movie_metadata.csv')
#print movie.head()
movie_num=pd.DataFrame()
movie.columns
for column in movie.columns:
    if isinstance(movie.ix[1,column],str)==False:
        movie_num.ix[:,column]=movie.ix[:,column]
movie_num=movie_num.fillna(value=0)       
from sklearn.preprocessing import StandardScaler
x_std=StandardScaler().fit_transform(movie_num.values)
from matplotlib import pyplot as plt
#fig=plt.figure(figsize=(8,8))
import seaborn as sns
cor= movie_num.corr()
sns.heatmap(cor)
mean_vec=np.mean(x_std,axis=0)
cov_mat=np.cov(x_std.T)
eig_vals,eig_vects=np.linalg.eig(cov_mat)
eig_pairs=[(eig_vals[i],eig_vects[:,i]) for i in range(len(eig_vals))]
eig_pairs.sort(key=lambda x:x[0],reverse=True)
percent=[i*100/sum(eig_vals) for i in sorted(eig_vals,reverse=True)]
summ=np.cumsum(percent)
plt.figure(figsize=(8,6))
plt.bar(range(len(percent)),percent)
plt.step(range(16),summ)
from sklearn.decomposition import PCA
pca=PCA(n_components=9)
final=pca.fit_transform(x_std)
plt.figure(figsize=(6,6))
plt.scatter(final[:,0],final[:,1])
from sklearn.cluster import KMeans
kmeans=KMeans(n_clusters=3)
x_clustered=kmeans.fit_predict(final)
rgb={0:'r',1:'b',2:'g'}
color=[rgb[i] for i in x_clustered]
plt.scatter(final[:,0],final[:,1],c=color)
df=pd.DataFrame(final)
df=df[[0,1,2]]
df['X_cluster']=x_clustered
sns.pairplot(df,hue='X_cluster',size=1.85)
