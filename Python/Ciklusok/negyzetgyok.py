x = float(input("x: "))

# Kezdeti intervallum : [0; x]
bal = 0
jobb = x
# felezo = (bal + jobb) / 2
print (bal, jobb)
for i in range (50) :
    felezo = (bal + jobb) / 2
    if felezo * felezo < x : #jobban megyünk tovább
        bal = felezo
    else:
        # balban megyünk tovább
        jobb = felezo
print (x, "négyzetgyöke: ", round(felezo, 4))






