a=int(input("masukkan batas bawah : "))
b=int(input("masukkan batas atas : "))

for x in range(a,b):
    for y in range(1,x):
        print("x",end=" ")
    print("") #pindah baris