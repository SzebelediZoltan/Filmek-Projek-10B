# Válogassuk ki a páros és páratlanszámokat
x=[7, 3, 4, 2, 1, 0, -8]

# Szetválogatás tétele:
paros=[]
paratlanok=[]
for i in range(len(x)):
    if x[i]%2==0:
        paros.append(x[i])
    else:
        paratlanok.append(x[i])

print(x)
print(paros)
print(paratlanok)