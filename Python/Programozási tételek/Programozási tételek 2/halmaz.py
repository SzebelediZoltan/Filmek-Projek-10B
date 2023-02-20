# Halmazkeszites tetel v. Egyediek kivalogatasa
def egyediek_kivalogatasa(lista:list):
    h=[]
    for i in range(len(lista)):
        if not bennevan(h, lista[i]):
            h.append(lista[i])
    return h
lista=[8,7,5,8,45,87,5,5,74,8,8,44,5,8,7,5,4,88,4,5,857,8]

halmaz=egyediek_kivalogatasa(lista)




