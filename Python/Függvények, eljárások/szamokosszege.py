#Kerjunk be szamokat addig, amig 3-mal oszthatot nem kapunk. Irjuk ki az osszeguket!
lista=[]
def beolvas(x):
    n=int(input())
    while not (n%3==0):
        x.append(n)
        n=int(input())


def osszeg(l):
    osszeg=0
    for i in range(len(l)):
        osszeg+= l[i]
    return osszeg

def kiir (s):
    print("A lista elemeinek osszege", s)


lista=[]
beolvas(lista)
s=osszeg(lista)
kiir(s)