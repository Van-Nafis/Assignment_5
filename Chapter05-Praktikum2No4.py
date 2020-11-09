kolom=5
baris=5

i=1
while(i<baris):
    j=5
    while(j<=kolom):
        print('* '*(j))
        j=j-1
        if j==0:
            break
    i=i+5
