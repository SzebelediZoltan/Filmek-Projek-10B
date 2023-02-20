fr=open("emberek.csv", "r")
emberek=fr.readlines()
# print(emberek)
nevek=[]
korok=[]
for i in range (len(emberek)):
    sor=emberek[i].split(";")
    nevek.append(sor[0])
    korok.append(int(sor[1]))
fr.close()