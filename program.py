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
    menu_jel()
    print("1-Legjobb film (A legjobb besorolást kapott film)")
    print("2-Legrosszabb film (A legrosszabb besorolást kapott film)")
    print("3-Leghoszabb film (A leghosszabb film)")
    print("4-Legjobb film (A legrövidebb film)")
    print("5-Megadott hosszú filmek (Egy megadott intervallumban kilistázza neked a filmeket)")
    print("6-Családbarát film (Első családbarát film)")
    print("6-Adatokkal kapcsolatos menu")
    print(-------------------------)
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
        adatok_menu(nevek, hosszak, ertekelesek, csaladbaratok)

def adatok_menu(nevek, hosszak, ertekelesek, csaladbaratok):
    menu_jel()
    print("1-Összes film darabszám")
    print("2-Össze percnyi film (nap/óra/perc)")
    print("3-Összes családbarát film")
    print("4-Összes NEM családbarát film")
    
def menu_jel():
    print("----------MENU----------")

def main():
    nevek=[]
    hosszak=[]
    ertekelesek=[]
    csaladbaratok=[]
    beolvas(nevek, hosszak, ertekelesek, csaladbaratok)
    menu(nevek, hosszak, ertekelesek, csaladbaratok)

main()