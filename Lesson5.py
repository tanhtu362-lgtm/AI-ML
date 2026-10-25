import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import mean_squared_error

np.random.seed(42)
X = np.linspace(0, 10, 40).reshape(-1, 1)
Y = 2 * X.ravel() + np.sin(2 * X.ravel()) * 3
Y = Y + np.random.normal(0, 1, size=40)

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.25, random_state=42)
# Thu cac bac da thuc khac nhau
for degree in [1, 14, 15]:
    model = make_pipeline(PolynomialFeatures(degree=degree), LinearRegression())
    model.fit(X_train, Y_train)
    train_predictions = model.predict(X_train)
    test_predictions = model.predict(X_test)
    
    train_mse = mean_squared_error(Y_train, train_predictions)
    test_mse = mean_squared_error(Y_test, test_predictions)
    
    
print("Bac da thuc:", degree)
print("Train MSE:", round(train_mse, 2))
print("Test MSE:", round(test_mse, 2))