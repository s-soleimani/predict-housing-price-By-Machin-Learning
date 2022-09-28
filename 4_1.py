from sklearn.model_selection import cross_val_score
scores = cross_val_score(tree_reg,final,df_label,scoring ="neg_mean_squared_error",cv = 10)
tree_rmse_scores = np.sqrt(-scores)

def display_scores(scores,model_name):
    print("==========" , model_name , "=============")
    print("scores :" , scores)
    print("mean :",scores.mean())
    print("standard deviation :" , scores.std())
    print("----------------------------------")
    
display_scores(tree_rmse_scores , "Decision Tree Regression")  

