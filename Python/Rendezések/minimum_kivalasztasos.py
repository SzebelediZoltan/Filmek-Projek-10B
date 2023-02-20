def minindex(x:list, i:int):
    mini=i
    for j in range(i+1, len(x)):
        if x[j] <x[mini]:
            mini= j
    return mini


#Haladjunk vegig a tombon es az aktualis elemet csereljuk meg a hatralevok minimumaval.
def rendezes_minimum(x):
    for i in range(len(x)-1):
        mini=minindex(x, i) #i-edik legkisebb indexét adja visssza
        x[i], x[mini]= x[mini], x[i] #csere
        # segedvaltozo= x[i]
        # x[i]= x[mini]
        # x[mini]=segedvaltozo


def main():
    x=[3, 5, 2, 1, 3]
    print(x)
    rendezes_minimum(x)
    print(x)


# main()