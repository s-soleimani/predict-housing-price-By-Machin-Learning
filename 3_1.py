from sklearn.linear_model import LinearRegression
Lin_reg = LinearRegression()
Lin_reg.fit(final , df_label)
sample_data_prepared =final.iloc[:4]
sample_data_prepared
print("predictions : \t",Lin_reg.predict(sample_data_prepared))
sample_labels = df_label . iloc[:4]
print("labels :\t\t" , list(sample_labels))
from sklearn.metrics import mean_squared_error
housing_predictions = Lin_reg.predict(final)
Lin_mse = mean_squared_error(df_label , housing_predictions)
Lin_rmse = np.sqrt(Lin_mse)
Lin_rmse 

