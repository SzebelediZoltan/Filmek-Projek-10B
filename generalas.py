from random import randint

def beolvasas(nevek):
    fr = open("film_nevek.txt", "r")
    sor = fr.readline().strip()
    while sor != "":
        nevek.append(sor)
        sor = fr.readline().strip()
    fr.close()
    
def generalas(nevek):
    fw = open("filmek.txt", "w")
    for i in range(len(nevek)):
        nev = nevek[i]
        hossz = randint(90, 210)
        ertekeles = randint(2, 20) / 2
        csaladbarat = randint(0, 1)
        
        fw.write(nev + " " + str(hossz) +" "+ str(ertekeles)+" "+str(csaladbarat)+"\n")
    fw.close()

def main():
    nevek = []
    beolvasas(nevek)
    generalas(nevek)
    
main()