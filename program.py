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
def main():
    nevek=[]
    hosszak=[]
    ertekelesek=[]
    csaladbaratok=[]
    beolvas(nevek, hosszak, ertekelesek, csaladbaratok)
    print(nevek, hosszak, ertekelesek, csaladbaratok)

main()