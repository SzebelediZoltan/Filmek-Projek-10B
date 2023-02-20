fr= open("adatok.txt", "r")
szamok=fr.read().split("")
# szamok= list(map(int, szamok))
for i in range (len(szamok)):
    szamok[i]=int(szamok[i])
print(szamok)
fr.close()