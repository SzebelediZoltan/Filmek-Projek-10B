def fiuk_lanyok_szetvalogat(nemek:list, fiuk:list, lanyok:list):
    for i in range(len(nemek)):
        if nemek[i]=="f":
           fiuk.append(i)
        else:
            lanyok.append(i)

def ki(lista:list, sorszamok:list):
    for i in range(len(sorszamok)):
        print(lista[sorszamok[i]], end=" ")
    print()


nevek=["Bela", "Feri", "Sanyi", "Erzsebet", "Juli", "Soma", "Hermione"]
nemek=["f","f","f","n", "n","f","n"]

fiuk=[]
lanyok=[]
fiuk_lanyok_szetvalogat(nemek, fiuk, lanyok)
print(fiuk)
print(lanyok)
ki(nevek, fiuk)
ki(nevek, lanyok)