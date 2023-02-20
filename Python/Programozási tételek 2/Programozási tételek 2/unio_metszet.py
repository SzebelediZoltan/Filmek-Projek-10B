def metszet_kepzes(a:list, b:list):
    m=[]
    for i in range(len(a)):
        if a[i] in b:
            m.append(a[i])
    return m

def unio_kepzes(a:list, b:list):
    u=[]
    for i in range(len(a)):
        u.append(a[i])
    for i in range(len(b)):
        if b[i] not in a:
            u.append(b[i])
        
    return u

def a_minusz_b_kepzes(a:list, b:list):
    d=[]
    ...
    return d
matekosok = ["Anna", "Béla", "Csaba", "Dóra", "Erik", "Ferenc"]
progosok = ["Ferenc", "József", "Dóra", "Anna", "Csaba"]

metszet= metszet_kepzes(matekosok, progosok)
unio=unio_kepzes(matekosok, progosok)
unio=unio_kepzes(matekosok, progosok)

print(unio)
print(metszet)

def metszet(a:list, b:list):
    return ([x for x in a if x in b])


csak_matekos= a_minusz_b_kepzes(matekosok, progosok)


# KEdves tanar ÚR tudom tudom nagyon sokat hibazok mostanag de bocsaanartt szertetnek kerni ! Ha netan leszophatnam megadja az 5ost? koszonom ! barbit megtszek Udv n = input("Mate!")