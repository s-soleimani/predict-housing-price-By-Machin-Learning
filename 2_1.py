
data["total_rooms_per_households"] = data["total_rooms"]/data["households"]
data["total_bedrooms_per_total_rooms"] = data["total_bedrooms"] / data["total_rooms"]
data["population_per_households"] = data["population"]/data["households"]

corr_matrix = data.corr()
corr_matrix["median_house_value"].sort_values(ascending = False)
df = train_set.copy()
df_label = df["median_house_value"].copy()
df = df.drop("median_house_value" , axis =1)

df_num = df.drop("ocean_proximity" , axis = 1)

median = df_num["total_bedrooms"].median()
df_num["total_bedrooms"].fillna(median)
imputer = SimpleImputer(missing_values=np.nan , strategy = 'median')
imputer.fit(df_num)
x=imputer.transform(df_num)
df_num_impute_tr = pd.DataFrame(x , columns = df_num.columns)
df_num_impute_tr.head()

