n= int(input())
varos= []
erkezes=[]
indulas=[]
for i in range (n):
    sor = (input().split())
    varos.append(sor[0])
    indulas.append(int(sor[1]))
    erkezes.append(int(sor[2]))
# print (v)
i = 0

while i<n and not(varos[i] == "Szekesfehervar" and indulas[i] == -1):
    i+=1
if i < n :
    print(erkezes[i])
else:
    print("-1")

