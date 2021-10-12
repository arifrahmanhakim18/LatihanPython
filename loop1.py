bawah=int(input("masukkan batas bawah : "))
atas=int(input("masukkan batas atas : "))

for x in range(bawah,atas+1) :
    if (x%2)!=0 :
        print(x, end="")