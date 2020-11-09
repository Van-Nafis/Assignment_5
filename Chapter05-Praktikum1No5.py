#Gaji pokok
A=10000000
B=8500000
C=7000000
D=5500000


a=(10000000*97.5/100)
b=(8500000*98/100)
c=(7000000*98.5/100)
d=(5500000*99/100)


AA=(int(input("Masukan kode karyawan = ")))
BB=(str(input("Masukan nama karyawan = ")))
CC=(str(input("Masukan golongan = ")))
DD=int(input("Masukan status (1:menikah, 2:belum) = "))
if(DD==1):
    EE=int(input("Masukan jumlah anak = "))
else:
    print()

TIS=10/100
TA=EE*5/100

print("=========================================")
print("STRUK RINCIAN GAJI KARYAWAN")
print("-----------------------------------------")
print("Nama Karyawan = ",BB)
print("Golongan = ",CC)
if(DD==1):
    print("Status Menikah = Menikah")
elif(DD==2):
    print("Status Menikah = Belum")
    
if(DD==1):
    print("Jumlah Anak = ",EE)
else:
    print()
print("-----------------------------------------")

#Gaji Pokok
if(CC=="A"):
    print("Gaji Pokok       = Rp  10000000.0")
elif(CC=="B"):
    print("Gaji Pokok       = Rp   8500000.0")
elif(CC=="C"):
    print("Gaji Pokok       = Rp   7000000.0")
elif(CC=="D"):
    print("Gaji Pokok       = Rp   5500000.0")

#Tunjangan Istri/Suami
if(CC=="A"):
    print("Tunjangan Istri/Suami = Rp",A*10/100)
elif(CC=="B"):
    print("Tunjangan Istri/Suami = Rp",B*10/100)
elif(CC=="C"):
    print("Tunjangan Istri/Suami = Rp",C*10/100)
elif(CC=="D"):
    print("Tunjangan Istri/Suami = Rp",D*10/100)

#Tunjangan Anak
if(DD==1):
    if(CC=="A"):
        print("Tunjangan Anak = Rp",A*5/100*EE)
    elif(CC=="B"):
        print("Tunjangan Anak = Rp",B*5/100*EE)
    elif(CC=="C"):
        print("Tunjangan Anak = Rp",C*5/100*EE)
    elif(CC=="D"):
        print("Tunjangan Anak = Rp",D*5/100*EE)

print("-----------------------------------------")

#Gaji Kotor
if(CC=="A"):
    print("Gaji Kotor = ",A + A*TIS + A*TA)
elif(CC=="B"):
    print("Gaji Kotor = ",B + B*TIS + B*TA)
elif(CC=="C"):
    print("Gaji Kotor = ",C + C*TIS + C*TA)
elif(CC=="D"):
    print("Gaji Kotor = ",D + D*TIS + D*TA)

#Potongan
if(CC=="A"):
    print("Potongan (2,5%) = Rp",(A + A*TIS +A*TA)*2.5/100)
elif(CC=="B"):
    print("Potongan (2,0%) = Rp",(B + B*TIS +B*TA)*2.0/100)
elif(CC=="C"):
    print("Potongan (1,5%) = Rp",(C + C*TIS +C*TA)*1.5/100)
elif(CC=="D"):
    print("Potongan (1,0%) = Rp",(D + D*TIS +D*TA)*1.0/100)


print("-----------------------------------------")
if(CC=="A"):
    print("Gaji Bersih = ",(A + A*TIS + A*TA)-(A + A*TIS +A*TA)*2.5/100)
elif(CC=="B"):
    print("Gaji Bersih = ",(B + B*TIS + B*TA)-(B + B*TIS +B*TA)*2.0/100)
elif(CC=="C"):
    print("Gaji Bersih = ",(C + C*TIS + C*TA)-(C + C*TIS +C*TA)*1.5/100)
elif(CC=="D"):
    print("Gaji Bersih = ",(D + D*TIS + D*TA)-(D + D*TIS +D*TA)*1.0/100)
