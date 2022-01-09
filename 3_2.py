#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#3_2
from sklearn.tree import DecisionTreeRegressor
tree_reg = DecisionTreeRegressor()
tree_reg.fit(final,df_label)
housing_predictions = tree_reg.predict(final)
tree_mse = mean_squared_error(df_label,housing_predictions)
tree_rmse = np.sqrt(tree_mse)
tree_rmse

