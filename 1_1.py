#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#1_1
import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split
from pandas.plotting import scatter_matrix
from sklearn.impute import SimpleImputer
from sklearn.base import BaseEstimator,TransformerMixin
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder

housing = pd.read_csv('housing.csv')
train_set , test_set = train_test_split(housing , test_size = 0.2 , random_state = 32)

data  = train_set.copy()
data.plot(kind = "scatter" , x= "longitude" , y = "latitude" ,s = data["population"]/30 , c=data["median_house_value"],cmap = plt.get_cmap("jet") ,figsize = (10 ,7) , alpha = 0.2)

