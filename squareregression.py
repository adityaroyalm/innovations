# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 16:06:23 2018

@author: aditya royal
"""
import pandas as pd
import numpy as np
df=pd.read_csv('y.csv')
def divide(df,x,y):
    sum_columns=np.array(df.loc[:,x].values)+np.array(df.loc[:,y].values)
    df.loc[:,'xy']=sum_columns
    total_max=[(index,xy_max) for index,xy_max in enumerate(df.loc[:,'xy']) if xy_max == max(df.loc[:,'xy'])]
    x_max=[(index,x_max) for index,x_max in enumerate(df.loc[:,x]) if x_max == max(df.loc[:,x])]
    y_max=[(index,y_max) for index,y_max in enumerate(df.loc[:,y]) if y_max == max(df.loc[:,y])]
    total_min=[(index,xy_min) for index,xy_min in enumerate(df.loc[:,'xy']) if xy_min == min(df.loc[:,'xy'])]
print(total_min,x_max,total_max,y_max)
divide(df,'num_critic_for_reviews','duration')
#np.linalg.det()
mat1[:,1]=np.array(total_max[0]^2+total_max[1]^2,x_max[0]^2+x_max[1]^2,total_min[0]^2+total_min[1]^2)
mat1[:,2]=np.array(total_max[1],x_max[1],total_min[1])
mat1[:,3]=np.ones(3)
mat2[:,1]=np.array(total_max[0],x_max[0],total_min[0])
mat2[:,2]=np.array(total_max[1],x_max[1],total_min[1])
mat2[:,3]=np.ones(3)
mat3[:,1]=np.array(total_max[0]^2+total_max[1]^2,x_max[0]^2+x_max[1]^2,total_min[0]^2+total_min[1]^2)
mat3[:,2]=np.array(total_max[0],x_max[0],total_min[0])
mat3[:,3]=np.ones(3)


#R='????'
#cent_x='????'
#cent_y='?????'
#df.loc[:'value']=(np.array(df[:,'x'])-cent_x)^2+(np.array(df[:,'y'])-cent_y)^2-R^2
#circle_in=df.loc[df.loc[:,'value']>0,'value']
        
