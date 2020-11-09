a=int(input("Masukan Nilai Bhs Indonesia ="))
b=int(input("Masukan Nilai IPA ="))
c=int(input("Masukan Nilai Matematika ="))
if(a<0)or(b<0)or(c<0):
    print("Maaf input anda tidak valid")
elif(60<a<=100)and(60<b<=100)and(70<c<=100):
    print("LULUS")
else:
        print("TIDAK LULUS")
        print("Sebab")
        if(a<60):
            print("Nilai bahasa Indonesia kurang dari 60")
        if(b<60):
            print("Nilai IPA kurang dari 60")
        if (c<70):
            print("Nilai Matematika kurang dari 70")


