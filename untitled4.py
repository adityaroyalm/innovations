# -*- coding: utf-8 -*-
"""
Created on Fri Mar 03 18:06:27 2017

@author: aditya royal
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Mar 01 10:28:59 2017

@author: aditya royal
"""
from sklearn.svm import SVC
import numpy as np
import pandas as pd
import csv
from StringIO import StringIO
from pandas import DataFrame as df
#train=pd.read_csv('C:/Users/aditya royal/Desktop/MLsoftaware_projects/titanic/train.csv')
#train = train.drop(['Survived'], axis=1)
#x_train = np.array(train)
#titanic=np.genfromtxt('C:/Users/aditya royal/Desktop/MLsoftaware_projects/titanic/train.csv',skip_header=1,delimiter=',',dtype=None)
csv_open=open('C:/Users/aditya royal/Desktop/MLsoftaware_projects/titanic/train.csv','rb')
csv_obj=csv.reader(csv_open)
csv_obj.next()
data=[]
for row in csv_obj:
    data.append(row)
truth=df(data).fillna(0)