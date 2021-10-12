from functools import reduce
# Map sebuah data dengan fungsi kuadrat
data=[1,2,3,4,5]
data2=["pisang","mangga","pepaya","salak","jeruk","durian"]

def kuadrat(x):
    return x**2

hasil=map(kuadrat,data)
print(list(hasil))

# Map kuadrat menggunakan lambda
hasil2=map(lambda x: x**2,data)
print(list(hasil2))

# Proses map dan filter untuk bilangan tidak sama dengan 4
hasil=map(lambda x : x !=4,data)
print(list(hasil))

hasil=filter(lambda x : x !=4,data)
print(list(hasil))

# Mencari bilangan terbesar
print(reduce(max,data))

#Index untuk akses elemen
print("Data pertama : ",data2[0])
print("Data terakhir : ",data2[-1])

#Contoh Slicing
print(data2)
print("")
print("Data [0:2] --> dari awal hingga sebelum index 2 : ",data2[0:2])
print("Data [:3] --> 3 data pertama : ",data2[:3])
print("Data [-3] --> 3 data terakhir : ",data2[-3:])
print("Data [::2] --> lompat dua, mulai elemen pertama : ",data2[::2])
print("Data [3::2] --> lompat dua, mulai index ke 3: ",data2[3::2])
print("Data [-2::1] --> lompat satu ke kanan, mulai indeks ke -2: ",data2[-2::1])
print("Data [-2::-1] --> lompat satu ke kiri, mulai indeks ke -2: ",data2[-2::-1])

