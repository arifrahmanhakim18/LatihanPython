selesai = False

while not selesai :
    angka=int(input("Masukkan angka : "))
    if (angka%2)==0 :
        print("genap")
    else:
        print("ganjil")
    lanjut=input("lagi ? (ya/tidak) : ")
    if lanjut=="tidak" :
        selesai=True
