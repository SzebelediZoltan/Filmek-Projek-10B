def paros_kivalogatasa(x):
    y=[]
    for i in range(len(x)):
        if x[i]%2==0:
            y.append(x[i])
    return y
    


x=[7, 3, 4, 2, 1, 0, -8]

# Kiválogatás tétele:
paros=paros_kivalogatasa(x)

print(paros)