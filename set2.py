# Operasi dasar elemen Set
merekMobil = {"avanza","xenia","expander","ertiga"}
mobilku = {"avanza","xenia"}

if mobilku.issubset(merekMobil):
    print("Set mobilku adalah subset merekMobil")

merekMobil.add("mobilio")
print("setelah ditambahkan mobilio (add) : ", merekMobil)

merekMobil.remove("mobilio")
print("setelah dikurangi mobilio (remove) : ",merekMobil)

merekMobil.update(["avanza","sigra"])
print("Diupdate dengan avanza dan sigra : ",merekMobil)

merekMobil.difference_update(mobilku)
print("Difference update: ", merekMobil)