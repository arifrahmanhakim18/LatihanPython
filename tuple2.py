data=("satu","dua","tiga","empat","lima","enam","tujuh","delapan")
print("Data Tuple : ",data)

i=0
hitungA=0
for x in data:
    for y in data[i]:
        if y=="a":
            hitungA=hitungA+1
    i=i+1

print("jumlah huruf 'a' ada : ",hitungA)