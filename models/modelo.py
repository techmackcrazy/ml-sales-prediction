

data.to_csv('./base.csv')

X=data.iloc[:,:-1]
y=data.iloc[:,-1]

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.3,random_state=100)

LR=LinearRegression()

LR.fit(X_train,y_train)
y_pred=LR.predict(X_test)


ridge = Ridge()
param_grid_ridge = {'alpha': [0.01, 0.1, 1, 10, 100]}
grid_search_ridge = GridSearchCV(estimator=ridge, param_grid=param_grid_ridge, cv=5, scoring='r2')
grid_search_ridge.fit(X_train, y_train)
best_ridge_model = grid_search_ridge.best_estimator_
print("Best parameters for Ridge Regression: ", grid_search_ridge.best_params_)
print("Best R2 score for Ridge Regression: ", grid_search_ridge.best_score_)

lasso = Lasso()
param_grid_lasso = {'alpha': [0.01, 0.1, 1, 10, 100]}
grid_search_lasso = GridSearchCV(estimator=lasso, param_grid=param_grid_lasso, cv=5, scoring='r2')
grid_search_lasso.fit(X_train, y_train)
best_lasso_model = grid_search_lasso.best_estimator_
print("Best parameters for Lasso Regression: ", grid_search_lasso.best_params_)
print("Best R2 score for Lasso Regression: ", grid_search_lasso.best_score_)

elastic_net = ElasticNet()
param_grid_enet = {
    'alpha': [0.01, 0.1, 1, 10, 100],
    'l1_ratio': [0.1, 0.3, 0.5, 0.7, 0.9]
}
grid_search_enet = GridSearchCV(estimator=elastic_net, param_grid=param_grid_enet, cv=5, scoring='r2')
grid_search_enet.fit(X_train, y_train)
best_enet_model = grid_search_enet.best_estimator_
print("Best parameters for Elastic Net: ", grid_search_enet.best_params_)
print("Best R2 score for Elastic Net: ", grid_search_enet.best_score_)

final_elastic_net_model = ElasticNet(alpha=10, l1_ratio=0.1)
final_elastic_net_model.fit(X_train, y_train)

mae=mean_absolute_error(y_test,y_pred)
mae

# squared for for rmse 
mse=mean_squared_error(y_test,y_pred,squared=False)
mse

r2_score(y_test,y_pred)

# Evaluate the model on the test set [step 7.5]
y_pred = final_elastic_net_model.predict(X_test)
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)




plt.figure(figsize=(10, 6))
sns.scatterplot(x=y_test, y=y_pred, alpha=0.6)
sns.lineplot(x=[y_test.min(), y_test.max()], y=[y_test.min(), y_test.max()], color='red', linestyle='--')
plt.xlabel("Actual Values")
plt.ylabel("Predicted Values")
plt.title("Actual vs Predicted Values with Line of Best Fit")
plt.show()