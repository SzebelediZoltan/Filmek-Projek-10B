# Halmazkeszites tetel v. Egyediek kivalogatasa
def bennevan(lista:list, elem:int):
    i=0
    while i < len(lista) and not (lista[i== elem]):
        i+=1
    return i < len(lista)

def egyediek_kivalogatasa(lista:list):
    h=[]
    for i in range(len(lista)):
        if lista[i] not in h:
            h.append(lista[i])
    return h
lista=[8,7,5,8,45,87,5,5,74,8,8,44,5,8,7,5,4,88,4,5,857,8]

halmaz=egyediek_kivalogatasa(lista)
print(halmaz)




