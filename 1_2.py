#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#1_2
corr_matrix = data.corr()
corr_matrix["median_house_value"].sort_values(ascending = False)
features = ["median_house_value","median_income","total_rooms","housing_median_age"]
scatter_matrix(data[features],figsize = (15,10))
plt.show
data.plot(kind = "scatter", x ="median_income" , y ="median_house_value" , figsize = (10,7) , alpha = 0.4)

