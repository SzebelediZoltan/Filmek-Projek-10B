n = int(input())
fajtak = []
mennyisegek = []

for i in range (n) :
    fajta=input()
    fajtak.append(fajta)
    mennyiseg= input()
    mennyisegek.append(int (mennyiseg))
print (mennyisegek, fajtak)


# s = 0
# elsoFajta= fajtak [0]
# for i in range (n):
#     if fajtak[i] == elsoFajta:
#         s += mennyisegek [i]

'''
s = 0
for i in range (n):
    if fajtak[i] == fajtak [0]:
        s += mennyisegek [i]
'''
s = mennyisegek [0]
for i in range (1,n):
    if fajtak [i] == fajtak [0]:
        s += mennyisegek [i]
print(s)