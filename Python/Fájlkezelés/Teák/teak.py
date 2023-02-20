
def beolvas(gy:list, m:list):
    fr=open("teak.txt", "r")
    felesleg=fr.readline()
    gyarto=fr.readline()
    mennyiseg=fr.readline()
    while gyarto!="":
        gy.append(gyarto.srtip())
        m.append(int(mennyiseg))
        gyarto=fr.readline()
        mennyiseg=fr.readline()
    fr.close()
def main():
    gyartok,mennyisegek=[] ,[]
    beolvas(gyartok, mennyisegek)
    # print(gyartok)
    # print(mennyisegek)
    osszeg_ki(gyartok, mennyisegek)

main()