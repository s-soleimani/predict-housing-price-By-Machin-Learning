rooms_ix , bedroom_ix , population_ix , houseold_ix = 3,4,5,6
class CombinedAttributesAdder(BaseEstimator,TransformerMixin):
       def fit(self, X , y = None):
           return self
       def transform(self,X,y = None):
           rooms_per_houseold = X[:,rooms_ix]/X[:,houseold_ix]
           population_per_houseold = X[:,population_ix]/X[:,houseold_ix]
           bedrooms_per_room =  X[:,bedroom_ix] / X[:,rooms_ix]
           return np.c_[X,rooms_per_houseold ,population_per_houseold, bedrooms_per_room]
           
custom = CombinedAttributesAdder()
data_custom_tr_tmp = custom.transform(df_num_impute_tr.values)
data_custom_tr = pd.DataFrame(data_custom_tr_tmp)
columns = list(df_num_impute_tr.columns)

columns.append("rooms_per_houseold")
columns.append("population_per_houseold")
columns.append("bedrooms_per_room")

data_custom_tr.columns = columns

data_custom_tr.describe()
feature_scale = StandardScaler()
data_num_scaled_tr = pd.DataFrame(feature_scale.fit_transform(data_custom_tr.values),columns = data_custom_tr.columns)

encoder_1hot = OneHotEncoder(sparse = False)
data_cat_1hot_tmp = encoder_1hot.fit_transform(df[["ocean_proximity"]])
data_cat_1hot = pd.DataFrame(data_cat_1hot_tmp)
data_cat_1hot.columns = encoder_1hot.get_feature_names(['prox'])
#data_cat_1hot.head()
final = pd.concat([data_num_scaled_tr , data_cat_1hot] , axis=1)
final.head()

