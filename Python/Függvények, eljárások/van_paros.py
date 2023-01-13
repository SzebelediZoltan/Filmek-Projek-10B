def vanParos(x):
    i=0
    while i < len(x) and not(x[i]%2==0):
        i+=1
    if i < len(x):
        return True
    else:
       return False

def ki(vanE):
    if vanE: 
        print("Van benne paros!")
    else:
        print("Nincs benne paros!")

    

szamok=[5, 2, 3, 7, 13]
vanE= vanParos(szamok)
ki(vanE)