# # Bai1
# from sklearn.linear_model import LinearRegression

# X = [[1], [2], [3], [4], [5]]
# # Ket qua thuc hien mo hinh tuyen tinh (Diem thi)
# y = [3, 4, 5, 7, 8]
# # Tao mo hinh model
# model = LinearRegression()
# model.fit(X, y) # Training
# # Du doan diem thi cho hoc sinh co diem so 6
# prediction = model.predict([[6]])
 
# print("Diem du doan:", prediction[0])
# print("He so goc: ", model.coef_[0])
# print("He so tu do", model.intercept_)


# # Bai 2 Phan loai co nhan KNN classification
# from sklearn.neighbors import KNeighborsClassifier

# # Chieu dai canh hoa (cm)
# X = [[1.0], [1.2], [3.0], [3.2]]
# # Nhan cua tung mau
# Y = ["Hoa mau do", "Hoa mau do", "Hoa mau vang", "Hoa mau vang"]
# # Tao mo hinh KNN
# model = KNeighborsClassifier(n_neighbors=1)
# model.fit(X,Y)

# prediction = model.predict([[3.5]])

# print("Loai hoa du doan:", prediction[0])

# # Bai 3 Phan loai khong nha KNN clustering
# from sklearn.cluster import KMeans

# # Khoi tao du lieu dac trung
# X = [
#     [1, 2],
#     [1, 3],
#     [2, 2],
#     [8, 8],
#     [9, 8],
#     [8, 9]
# ]

# # Yeu cau chia mo hinh thanh 2 nhom
# model = KMeans(n_clusters=2,random_state=42, n_init=10)
# # Training mo hinh
# model.fit(X)

# print("Cac nhom duoc chia:" , model.labels_)



# # Dataset,Features,label
# from sklearn.neighbors import KNeighborsClassifier
# # Khoi tao du lieu dac trung Features
# X = [
#     [1, 2],
#     [1, 3],
#     [2, 2],
#     [8, 8],
# ]

# # Khoi tao nhan Label
# Y = [
#     "Hoa Mau Do",
#     "Hoa Mau Trang",
#     "Hoa Mau Hong",
#     "Hoa Mau Vang"
# ]    

# # Xuat du lieu bang print xuat ra so luong mau du lieu

# print("So dac trung cua X la:", len(X))
# print("So nhan cua Y la: ", len(Y))

# print("Cac phan tu cua X la: ", X)
# print("Cac phan tu cua Y la: ", Y)

# print("So dac trung cua X la: ", len(X[0]))

# model = KNeighborsClassifier(n_neighbors=1)

# model.fit(X, Y)

# new_flower = [[1, 3]]

# prediction = model.predict(new_flower)

# print(prediction[0])


