data=("satu","dua","tiga","empat","lima","enam","tujuh","delapan")
dataAngka=(1,2,3,4,5,6)
dataCampur=(1,"budi",1996,("bekasi","jawa barat"),["sd","smp","sma"])
mhs1=("budi","majalengka","jawa barat","memangcing",17,"April",1996)

print("Tuple dataCampur : ",dataCampur)
print("")

#mengakses Tuple
print("Data Tuple : ",data)
print("elemen ke-1 : ",data[0])
print("elemen terakhir : ", data[-1])
print("tiga ada di index ke",data.index("tiga"))

#mengakses elemen di dalam elemen
print("isi keempat dari elemen pertama :",mhs1[0][3])

#pengulangan elemen Tuple
for y in mhs1:
    print(y)