print("Hai.. nama saya Mr. Lappie, saya telah memilih sebuah bilangan bulat secara acak antara 0 s/d 100. Silakan tebak ya!!!")
from random import randint
hitung=randint(0,100)

while True:
    tebakan=int(input("Tebakan Anda : "))
    if (tebakan<hitung):
        print("Hehehe... Bilangan tebakan anda terlalu kecil")
    elif (tebakan>hitung):
        print("Hehehe... Bilangan tebakan anda terlalu besar")
    else:
        print("Yeeee.... Bilangan tebakan anda benar :-)")
        break
