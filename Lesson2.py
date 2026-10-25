# import numpy as np

# # Danh sach trong python
# list1 = [1, 2, 3, 4, 5]
 
# # Chuyen danh sach sang numpy array
# arr = np.array(list1)

# print(arr)
# print("Tong la: ", np.sum(arr))
# print("Trung binh la: ", np.mean(arr))
# print("max la: ", np.max(arr))
# print("Min la: ", np.min(arr))

# Tao bang du lieu
import pandas as pd
# from sklearn.linear_model import LinearRegression

data = {
    "Name": ["An", "Hoa", "Binh", "Phuc"],
    "Hours": ["1", "2", None, "ba"],
    "Score": [6, 7, 8, 9],
}

df = pd.DataFrame(data)

print(df)
# print(df.head(2))
# print(df.shape)
# print(df["Hours"])
# print(df[df["Score"] > 8])
# print("Kiem tra kieu du lieu")
# print(df.info())

# X = df[["Hours"]]
# Y = df["Score"]
# model = LinearRegression()
# model.fit(X, Y)

# prediction = model.predict(pd.DataFrame({"Hours": [5]}))
# print("Diem du doan: ", prediction[0])

# Lam sach du lieu

# kiem tra du lieu bi thieu
print(df.isnull()) 
# Tong so o du lieu bi thieu
print(df.isnull().sum()) 
print(df["Hours"].isnull())

# Xoa dong du lieu bi thieu cu the la cac o trong null
print("Xoa du lieu bi thieu")
df_clean = df.dropna()
print(df_clean)
print("Chuyen du lieu thanh dang so")
df["Hours"] = pd.to_numeric(df["Hours"], errors="coerce")
print(df["Hours"])
print(df.isnull())

