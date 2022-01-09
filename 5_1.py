#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#5_1
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import GridSearchCV
import numpy as np
param_grid = [{'n_estimators':[3,4,6,10,30],'max_features':[2,6,8,15]}]
forest_reg = RandomForestRegressor()
param_grid

