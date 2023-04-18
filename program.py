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
    print(megfelelo_nevek)

def legjobb_film(ertekelesek):
    maxe=ertekelesek[0]
    maxi=0
    for i in range (1, len(ertekelesek)):
        if ertekelesek[i]> maxe:
            maxe=ertekelesek[i]
            maxi=i

def legrosszabb_film(ertekelesek):
    mine=ertekelesek[0]
    mini=0
    for i in range (1, len(ertekelesek)):
        if ertekelesek[i]< mine:
            mine=ertekelesek[i]
            mini=i

def leghosszabb_film(hosszak):
    maxe=hosszak[0]
    maxi=0
    for i in range (1, len(hosszak)):
        if hosszak[i]> maxe:
            maxe=hosszak[i]
            maxi=i

def legrövidebb_film(hosszak):
    mine=hosszak[0]
    mini=0
    for i in range (1, len(hosszak)):
        if hosszak[i]< mine:
            mine=hosszak[i]
            mini=i

def osszes_film(nevek):
    db=0
    for i in range(len(nevek)):
        db+=1

def osszes_perc(hosszak):
    perc=0
    for i in range(len(hosszak)):
        perc=hosszak[i]

def elso_csaladbarat(nevek, csaladbaratok):
    i=0
    while i < len(csaladbaratok) and not (csaladbaratok[i]==1 ):
        i+=1
    if i< len(csaladbaratok):
        print(nevek[i])
    else:
        print("Nincs családbarát film az adatbázisunkba.")

def menu(nevek, hosszak, ertekelesek, csaladbaratok):
    while True:
        ljobb_film = legjobb_film(nevek, ertekelesek)
        lrosszabb_film = legrosszabb_film(nevek, ertekelesek)
        lhosszabb_film = leghosszabb_film(nevek, hosszak)
        lrovidebb_film = legrövidebb_film(nevek, hosszak)
        inter_filmek = megadott_ido(nevek, hosszak)
        csb_film = elso_csaladbarat(nevek, csaladbaratok)
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
        menu_jel("s")
        if valasztas == 1:
            print(ljobb_film)
        elif valasztas == 2:
            print(lrosszabb_film)
        elif valasztas == 3:
            print(lhosszabb_film)
        elif valasztas == 4:
            print(lrovidebb_film)
        elif valasztas == 5:
            kiir(inter_filmek)
        elif valasztas == 6:
            print(csb_film)
        elif valasztas == 7:
            d1f()
        elif valasztas == 8:
            adatok_menu(nevek, hosszak, ertekelesek, csaladbaratok)

def adatok_menu(nevek, hosszak, ertekelesek, csaladbaratok):
    ossz_film = osszes_filmneve(nevek)
    ossz_filmdb = osszes_film(nevek)
    ossz_perc = osszes_perc(hosszak)
    ossz_csb = osszes_csaladbarat(nevek, csaladbaratok)
    ossz_n_csb = oszes_nem_csaladbarat(nevek, csaladbaratok)
    ossz_10 = tiztiz_filmek(nevek, ertekelesek)
    ossz_1 = tizegy_filmek(nevek, ertekelesek)
    menu_jel("a")
    print("1-Összes film")
    print("2-Összes percnyi film (nap/óra/perc)")
    print("3-Összes családbarát film")
    print("4-Összes NEM családbarát film")
    print("5-Összes 10/10-es film")
    print("6-Összes 10/1-es film")
    menu_jel("s")
    valasztas = int(input("Választás: "))
    menu_jel("s")
    if valasztas == 1:
        kiir(ossz_film)
        menu_jel("s")
        print(f"Összes film darabszam: {ossz_filmdb}")
    elif valasztas == 2:
        print(ossz_perc)
    elif valasztas == 3:
        kiir(ossz_csb)
    elif valasztas == 4:
        kiir(ossz_n_csb)
    elif valasztas == 5:
        kiir(ossz_10)
    elif valasztas == 6:
        kiir(ossz_1)

    
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
        return "Nincs 10-es értékelést elért film az adatbázisunkban."
    else:
        return kivalogatott_nevek[i]
    

def main():
    nevek=[]
    hosszak=[]
    ertekelesek=[]
    csaladbaratok=[]
    beolvas(nevek, hosszak, ertekelesek, csaladbaratok)
    menu(nevek, hosszak, ertekelesek, csaladbaratok)

main()