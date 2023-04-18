def beolvas(nevek, hosszak, ertekelesek, csaladbaratok):
    fr=open("filmek.txt", "r")
    sor=fr.readline().strip().split()
    while sor != []:
        nevek.append(sor[0])
        hosszak.append(int(sor[1]))
        ertekelesek.append(float(sor[2]))
        csaladbaratok.append(int(sor[3]))
        sor=fr.readline().strip().split()
    fr.close()

def megadott_ido(nevek, hosszak):
    mine=int(input("Legrövidebb: "))
    maxe=int(input("Leghosszabb: "))
    megfelelo_nevek=[]
    for i in range(len(nevek)):
        if hosszak[i]>=mine and hosszak[i]<=maxe:
             megfelelo_nevek.append(nevek[i])
    return megfelelo_nevek

def legjobb_film(ertekelesek):
    maxe=ertekelesek[0]
    maxi=0
    for i in range (1, len(ertekelesek)):
        if ertekelesek[i]> maxe:
            maxe=ertekelesek[i]
            maxi=i
    return maxi

def legrosszabb_film(ertekelesek):
    mine=ertekelesek[0]
    mini=0
    for i in range (1, len(ertekelesek)):
        if ertekelesek[i]< mine:
            mine=ertekelesek[i]
            mini=i
    return mini

def leghosszabb_film(hosszak):
    maxe=hosszak[0]
    maxi=0
    for i in range (1, len(hosszak)):
        if hosszak[i]> maxe:
            maxe=hosszak[i]
            maxi=i
    return maxi

def legrövidebb_film(hosszak):
    mine=hosszak[0]
    mini=0
    for i in range (1, len(hosszak)):
        if hosszak[i]< mine:
            mine=hosszak[i]
            mini=i
    return mini

def osszes_film(nevek):
    db=0
    for i in range(len(nevek)):
        db+=1
    return db

def osszes_perc(hosszak):
    perc=0
    for i in range(len(hosszak)):
        perc=hosszak[i]

    nap = perc//1440
    perc = perc%1440
    óra = perc//60
    perc  = perc%60
    return nap, óra, perc

def elso_csaladbarat(nevek, csaladbaratok):
    i=0
    while i < len(csaladbaratok) and not (csaladbaratok[i]==1 ):
        i+=1
    if i< len(csaladbaratok):
        return (nevek[i])
    else:
        return("Nincs családbarát film az adatbázisunkba.")

def tizegy_filmek(nevek, ertekelesek):
    kivalogatott_nevek = []
    for i in range(len(ertekelesek)):
        if ertekelesek[i] == 1:
            kivalogatott_nevek.append(nevek[i])
    
    if len(kivalogatott_nevek) == 0:
        return("Nincs 1-es értékelést elért film az adatbázisunkban.")
    else:
        return(kivalogatott_nevek[i])

def osszes_filmneve(nevek):
    for i in range(len(nevek)):
        return(nevek[i])

def osszes_csaladbarat(nevek, csaladbaratok):
    csb=[]
    for i in range(len(csaladbaratok)):
        if csaladbaratok==1:
            csb.append(nevek[i])
    return csb
    
def osszes_nem_csaladbarat(nevek, csaladbaratok):
    csb=[]
    for i in range(len(csaladbaratok)):
        if csaladbaratok==0:
            csb.append(nevek[i])
    return csb

def kiir(lista):
    if type(list)==str:
        print(lista)
    else:
        for i in range(len(lista)):
            print(lista[i])
        

def menu(nevek, hosszak, ertekelesek, csaladbaratok):
    menu_jel("m")
    print("1-Legjobb film")
    print("2-Legrosszabb film")
    print("3-Leghoszabb film")
    print("4-Legrövidebb film")
    print("5-Megadott hosszú filmek (Egy megadott intervallumban kilistázza neked a filmeket)")
    print("6-Családbarát film (Első családbarát film)")
    print("7-DOBJ EGY FILMET")
    print("8-Adatokkal kapcsolatos menu")
    menu_jel("s")
    valasztas = int(input("Választás: "))
    if valasztas == 1:
        legjobb_film(ertekelesek)
    elif valasztas == 2:
        legrosszabb_film(ertekelesek)
    elif valasztas == 3:
        leghosszabb_film(hosszak)
    elif valasztas == 4:
        legrövidebb_film(hosszak)
    elif valasztas == 5:
        megadott_ido(nevek, hosszak)
    elif valasztas == 6:
        elso_csaladbarat(nevek, csaladbaratok)
    elif valasztas == 7:
        dobj_1_filmet(nevek, hosszak, ertekelesek, csaladbaratok)
    elif valasztas == 8:
        adatok_menu(nevek, hosszak, ertekelesek, csaladbaratok)
    else:
        fancy_lista(nevek, hosszak, ertekelesek, csaladbaratok)

def adatok_menu(nevek, hosszak, ertekelesek, csaladbaratok):
    menu_jel("a")
    print("1-Összes film")
    print("2-Összes film darabszám")
    print("3-Összes percnyi film (nap/óra/perc)")
    print("4-Összes családbarát film")
    print("5-Összes NEM családbarát film")
    print("6-Összes 10/10-es film")
    print("7-Összes 10/1-es film")
    print("-------------------------")
    valasztas = int(input("Választás: "))
    
def menu_jel(v="m"):
    if v == "m":
        print("----------MENU----------")
    elif v == "a":
        print("-------ADATOK-MENU-------")
    elif v == "s":
        print("-------------------------")
        
def fancy_lista(nevek, hosszak, ertekelesek, csaladbaratok, fajl="fajl.txt"):
    fw = open(fajl, "w")
    fw.write("------------------------- \n")
    for i in range(len(nevek)):
        fw.write("Film neve: " + nevek[i] + "\n")
        fw.write("Film hoszusaga percben: " + str(hosszak[i]) + "\n")
        fw.write("Film ertekelese: " + str(ertekelesek[i]) + "\n")
        if csaladbaratok[i] == 1:
            fw.write("Csaladbarat: Igen \n")
        else:
            fw.write("Csaladbarat: Nem \n")
            
        fw.write("------------------------- \n")
        
    fw.close()
    
def tiztiz_filmek(nevek, ertekelesek):
    kivalogatott_nevek = []
    for i in range(len(ertekelesek)):
        if ertekelesek[i] == 10:
            kivalogatott_nevek.append(nevek[i])
    
    if len(kivalogatott_nevek) == 0:
        print("Nincs 10-es értékelést elért film az adatbázisunkban.")
    else:
        for i in range(len(kivalogatott_nevek)):
            print(kivalogatott_nevek[i])
    

def main():
    nevek=[]
    hosszak=[]
    ertekelesek=[]
    csaladbaratok=[]
    beolvas(nevek, hosszak, ertekelesek, csaladbaratok)
    menu(nevek, hosszak, ertekelesek, csaladbaratok)

main()