szamok=[1, 2, 3, 4,5,6,7,8,9,10,11,12]
k=int(input())
x=[]

def nagyok_kivalogat(lista:list, k):
    for i in range(len(lista)):
        if lista[i]>k:
            x.append(i+1)
        # Nem működött 12-nél kisebb számoknál
        # else:
        #     x="A megadott szám nagyobb vagy egyenlő mint a többi szám!"
    return x


kiiras=nagyok_kivalogat(szamok, k)
print(kiiras, end=" ")








            
