
jumlah=int(input("Jumlah : "))
hargasatuan=int(input("harga : "))

def hitungTotal(a,b):
    return a*b
def hitungNet(c,d):
    return hitungTotal(c,d)-5000

if (hitungTotal(jumlah,hargasatuan)>50000):
    print(hitungNet(jumlah,hargasatuan))
else:
    print(hitungTotal(jumlah,hargasatuan))
