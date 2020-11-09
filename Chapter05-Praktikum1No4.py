
a=(10000000*97.5/100)
b=(8500000*98/100)
c=(7000000*98.5/100)
d=(5500000*99/100)
AA=(int(input("Masukan kode karyawan = ")))
BB=(str(input("Masukan nama karyawan = ")))
CC=(str(input("Masukan golongan = ")))

print("=========================================")
print("STRUK RINCIAN GAJI KARYAWAN")
print("-----------------------------------------")
print("Nama Karyawan = ",BB)
print("Golongan = ",CC)
print("-----------------------------------------")

if(CC=="A"):
    print("Gaji Pokok      :  Rp 10.000.000")
    print("Potongan (2.5%) :  Rp    250.000")
elif(CC=="B"):
    print("Gaji Pokok      :  Rp  8.500.000")
    print("Potongan  2.0%) :  Rp    170.000")
elif(CC=="C"):
    print("Gaji Pokok      :  Rp  7.000.000")
    print("Potongan (1.5%) :  Rp    105.000")
elif(CC=="D"):
    print("Gaji Pokok      :  Rp  5.500.000")
    print("Potongan (1.0%) :  Rp     55.000")

print("-----------------------------------------")
if(CC=="A"):
    print("Gaji Bersih = " + str(a))
elif(CC=="B"):
    print("Gaji Bersih = " + str(b))
elif(CC=="C"):
    print("Gaji Bersih = " + str(c))
elif(CC=="D"):
    print("Gaji Bersih = " + str(d))
