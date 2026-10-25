# import pandas as pd
# from sklearn.linear_model import LinearRegression
# from sklearn.model_selection import train_test_split
# # Tinh sai so
# from sklearn.metrics import mean_absolute_error

# data = {
#     "Hours": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
#     "Score": [2, 4, 5, 4, 6, 7, 8, 8, 10, 9]
# }

# df = pd.DataFrame(data)

# X = df[["Hours"]]
# Y = df["Score"]
# print(df["Hours"])
# model = LinearRegression()

# # chia du lieu
# X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)
# model.fit(X_train, Y_train)
# prediction = model.predict(X_test)
# # So Sanh du doan diem thuc te
# print("Diem thuc te: ", Y_test.to_list())
# print("Diem du doan la prediction: ", prediction)


# # print("So du lieu ban dau:", len(df))
# # print("So du lieu da train:", len(X_train))
# # print("So du lieu da test:", len(X_test))

# # print(X_train)
# # print("==============================")
# # print(Y_train)
# # print("==============================")
# # print(X_test)
# # print("==============================")
# # print(Y_test)

# # Tinh sai so
# mae = mean_absolute_error(Y_test, prediction)
# print(mae)


