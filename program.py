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
    ...

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