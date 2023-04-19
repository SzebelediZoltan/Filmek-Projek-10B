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
    menu_jel("s")
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
        perc+=hosszak[i]

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
        return(kivalogatott_nevek)

def osszes_filmneve(nevek):
    return nevek

def osszes_csaladbarat(nevek, csaladbaratok):
    csb=[]
    for i in range(len(csaladbaratok)):
        if csaladbaratok[i]==1:
            csb.append(nevek[i])
            
    if len(csb) == 0:
        return("Nincs családbarát film az adatbázisunkban.")
    else:
        return csb
    
def osszes_nem_csaladbarat(nevek, csaladbaratok):
    csb=[]
    for i in range(len(csaladbaratok)):
        if csaladbaratok[i]==0:
            csb.append(nevek[i])
    
    if len(csb) == 0:
        return("Nincs NEM családbarát film az adatbázisunkban.")
    else:
        return csb

def kiir(lista):
    if type(lista)==str:
        print(lista)
    else:
        for i in range(len(lista)):
            print(lista[i])
        

def menu(nevek, hosszak, ertekelesek, csaladbaratok):
    while True:
        ljobb_film_i = legjobb_film(ertekelesek)
        lrosszabb_film_i = legrosszabb_film(ertekelesek)
        lhosszabb_film_i = leghosszabb_film(hosszak)
        lrovidebb_film_i = legrövidebb_film(hosszak)
        csb_film = elso_csaladbarat(nevek, csaladbaratok)
        menu_jel("m")
        print("1-Legjobb film")
        print("2-Legrosszabb film")
        print("3-Leghoszabb film")
        print("4-Legrövidebb film")
        print("5-Megadott hosszú filmek (Egy megadott intervallumban kilistázza neked a filmeket)")
        print("6-Családbarát film (Első családbarát film)")
        print("7-LEPJ MEG")
        print("8-Adatokkal kapcsolatos menu")
        print("9-TESZT Menu")
        print("10-KILÉPÉS")
        menu_jel("s")
        valasztas = input("Választás: ")
        menu_jel("s")
        if valasztas == "1":
            print(nevek[ljobb_film_i])
        elif valasztas == "2":
            print(nevek[lrosszabb_film_i])
        elif valasztas == "3":
            print(nevek[lhosszabb_film_i])
        elif valasztas == "4":
            print(nevek[lrovidebb_film_i])
        elif valasztas == "5":
            kiir(megadott_ido(nevek, hosszak))
        elif valasztas == "6":
            print(csb_film)
        elif valasztas == "7":
            lm(nevek, hosszak, ertekelesek, csaladbaratok)
        elif valasztas == "8":
            adatok_menu(nevek, hosszak, ertekelesek, csaladbaratok)
        elif valasztas == "9":
            teszt_menu(nevek, hosszak, ertekelesek, csaladbaratok)
        elif valasztas == "10":
            quit()
        elif valasztas == "":
            print("Valamit meg is kéne adni")
        else:
            print("Adj meg lehetséges választ")
            
            
def teszt_menu(nevek, hosszak, ertekelesek, csaladbaratok):
    teszt = True
    while teszt:
        menu_jel("t")
        print("Melyik teszt fájlt szeretnéd használni?")
        print("1-be1.txt")            
        print("2-be2.txt")            
        print("3-be3.txt")
        print("4-KILÉPÉS")
        menu_jel("s")
        valasztas = input("Választás: ")
        menu_jel("s")
        if valasztas == "1":
            teszt_1()       
        elif valasztas == "2":
            teszt_2()       
        elif valasztas == "3":
            teszt_3()
        elif valasztas == "4":
            teszt = False
        elif valasztas == "":
            print("Valamit meg is kéne adni")
        else:
            print("Adj meg lehetséges választ")       

def teszt_1():
    menu_jel("t")
    fr = open("be1.txt", "r")
    sor= fr.readline().strip().split()
    while sor != [""]:
        sor=fr.readline().strip().split()
        
def teszt_2():
    menu_jel("t")
    fr = open("be2.txt", "r")
    sor= fr.readline().strip().split()
    while sor != [""]:
        sor=fr.readline().strip().split()
        
def teszt_3():
    menu_jel("t")
    fr = open("be3.txt", "r")
    sor= fr.readline().strip().split()
    while sor != [""]:
        sor=fr.readline().strip().split()
    

def lm(nevek, hosszak, ertekelesek, csaladbaratok):
    menu_jel("lm")
    valasztas = input("Több filmel is meglepjelek? (I vagy N): ")
    if valasztas == 'I':
        db = int(input("Mennyivel? (MAX: 500): "))
    
    menu_jel("lm")
    print("1-Lepj meg családbarát film(ekk)el")
    print("2-Lepj meg rövid film(ekk)el")
    print("3-Lepj meg hosszú film(ekk)el")
    print("4-Lepj meg jó film(ekk)el")
    print("5-Nekem aztán 8")
    menu_jel("s")
    valasztas = input("Választás: ")
    menu_jel("s")
    if valasztas == "1":
        lmcsf()
    elif valasztas == "2":
        lmrf()
    elif valasztas == "3":
        lmhf()
    elif valasztas == "4":
        lmjf()
    elif valasztas == "5":
        na8()
    elif valasztas == "":
        print("Valamit meg is kéne adni")
    else:
        print("Adj meg lehetséges választ")
        

def adatok_menu(nevek, hosszak, ertekelesek, csaladbaratok):
    ossz_film = osszes_filmneve(nevek)
    ossz_filmdb = osszes_film(nevek)
    ossz_ido = osszes_perc(hosszak)
    ossz_csb = osszes_csaladbarat(nevek, csaladbaratok)
    ossz_n_csb = osszes_nem_csaladbarat(nevek, csaladbaratok)
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
    valasztas = input("Választás: ")
    menu_jel("s")
    if valasztas == "1":
        kiir(ossz_film)
        menu_jel("s")
        print(f"Összes film darabszam: {ossz_filmdb}")
        valasztas = input("Szeretnéd Exportálni külön fájlba az adatokat? (I vagy N): ")
        if valasztas == "I":
            valasztas = input("Szeretnél saját nevet a fájlnak? (I vagy N): ")
            if valasztas == "I":
                fajl_nev = input("Mi legyen a neve? (A végére tedd ki a .txt-t): ")
                fancy_lista(nevek, hosszak, ertekelesek, csaladbaratok, fajl_nev)
            else:
                fancy_lista(nevek, hosszak, ertekelesek, csaladbaratok)
    elif valasztas == "2":
        print(f"{ossz_ido[0]} nap, {ossz_ido[1]} óra, {ossz_ido[2]} perc")
    elif valasztas == "3":
        kiir(ossz_csb)
    elif valasztas == "4":
        kiir(ossz_n_csb)
    elif valasztas == "5":
        kiir(ossz_10)
    elif valasztas == "6":
        kiir(ossz_1)
    elif valasztas == "":
        print("Valamit meg is kéne adni")
    else:
        print("Adj meg lehetséges választ")

    
def menu_jel(v="m"):
    if v == "m":
        print("----------MENU----------")
    elif v == "a":
        print("-------ADATOK-MENU-------")
    elif v == "s":
        print("-------------------------")
    elif v == "lm":
        print("-----------LM------------")
    elif v == "t":
        print("----------TESZT----------")
        
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
        return kivalogatott_nevek
    

def main():
    nevek=[]
    hosszak=[]
    ertekelesek=[]
    csaladbaratok=[]
    beolvas(nevek, hosszak, ertekelesek, csaladbaratok)
    menu(nevek, hosszak, ertekelesek, csaladbaratok)

main()