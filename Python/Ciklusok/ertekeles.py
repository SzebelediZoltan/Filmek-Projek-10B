n = int (input ("Pontszám: "))

if 0 <= n  <= 42 :
    print ("elégtelen")
elif 43 <= n <= 57 :
    print ("elégséges")
elif 58 <= n <= 72 :
    print ("közepes")
elif 73 <= n <= 87 :
    print ("jó")
elif 88 <= n <= 100 :
    print ("jeles")
else :
    print ("Nem 0-100 közötti számot adtál meg!")