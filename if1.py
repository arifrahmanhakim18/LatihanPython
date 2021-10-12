bil = int(input("Masukkan bilangan : "))

if (bil < 0) :
    print('Masukkan bilangan positif')
else : 
    if (bil % 2) == 0 :
        print("{0} adalah bilangan genap".format(bil))
    else :
        print("{0} adalah bilangan ganjil".format(bil))