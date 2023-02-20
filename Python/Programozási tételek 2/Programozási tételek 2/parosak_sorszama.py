# Válogassuk ki a páros számokat
x=[7, 3, 4, 2, 1, 0, -8]

# Kiválogatás tétele:
y=[]
for i in range(len(x)):
    if x[i]%2==0:
        y.append(i)


# Kiiras
# print(y)
# Sorszamok kiirasa
for i in range(len(y)):
    print(y[i]+1, end=" ")
# Ertekek kiirasa
print()
for i in range(len(y)):
    ind=y[i]
    print(x[ind], end=" ")