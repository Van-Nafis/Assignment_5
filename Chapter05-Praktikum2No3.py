hitung=0
sum=0
for i in range (0,100):
    bil=i+1
    if bil%2!=0:
        hitung=hitung+1
        sum=sum+bil
        print(i)
print("Banyaknya bilangan ganjil : " + str(hitung))
print("Jumlah seluruh bilangan ganjil : " + str(sum))
