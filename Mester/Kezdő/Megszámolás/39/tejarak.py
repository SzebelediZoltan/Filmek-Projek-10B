be = input()
lista = be.split()
szamok = list(map(int, lista))
# print(szamok)

n = szamok[0]
p = szamok[1]
q = szamok[2]

#tejarak beolvasasa
tejarak = []
for i in range(n):
    ar = int(input())
    tejarak.append(ar)
# print (tejarak)

db = 0 
for i in range (n) :
    if p <= tejarak [i] and tejarak [i] <= q :
        db += 1
print (db)
