#Beolvasas
ido = int (input ("Másodperc: ")) #3723

#Feldolgozas
ora = ido // 3600
ido = ido % 3600 #123
perc = ido // 60
masodperc = ido % 60 

#Kiiras
print ("Eltelt ido:", ora, "ora", perc, "perc", masodperc, "masodperc")