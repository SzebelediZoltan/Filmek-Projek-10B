from random import randint
from minimum_kivalasztasos import rendezes_minimum
from buborekos import buborékos
from os import system
from time import time
#Visszater egy "n" elemu listaval amiben [1,20] intervallumbol vannak random szamok
def feltolt(n):
    x=[]
    for i in range(n):
        x.append(randint(1,20))
    return x


def main():
    # Kepernyo torles:
    system("cls")
    x= feltolt(100)


    print("\nRendezes elott:")
    print(x)

    
    y=x.copy()
    start=time()
    rendezes_minimum(y)
    stop=time()
    print("\nMinimum-kivalasztasos:")
    print("Idő:",round(stop-start, 20) )

    y=x.copy()
    buborékos(y)
    print("\nBuborekos:")
    print(y)

    y=x.copy()
    y.sort()
    print("\nLista sort:")
    print(y)

    


main()