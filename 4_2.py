Linear_scores =  cross_val_score(Lin_reg,final,df_label,scoring ="neg_mean_squared_error",cv = 10)
Linear_rmse_scores = np.sqrt(-Linear_scores)
display_scores(Linear_rmse_scores,"Linear Regression")

