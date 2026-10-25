import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import (mean_absolute_error,
                             mean_squared_error, r2_score)

data = {
    "Hours": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "Score": [2, 4, 5, 4, 6, 7, 8, 8, 10, 9]
}

df = pd.DataFrame(data)

X = df[["Hours"]]
Y = df["Score"]
model = LinearRegression

X_train, X_test, Y_train, Y_test = train_test_split(
    X, Y, test_size=0.2, random_state=42
)

model = LinearRegression()
model.fit(X_train, Y_train)
predictions = model.predict(X_test)

print("Diem du thuc te: ", Y_test.to_list())
print("Diem du doan la: ", predictions)
mae = mean_squared_error(Y_test, predictions)
mse = mean_absolute_error(Y_test, predictions)
rmse = mse ** 0.5
r2_score = r2_score(Y_test, predictions)

print(mae)
print(mse)
print(rmse)
print(r2_score)


