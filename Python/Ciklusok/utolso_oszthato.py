n = int (input("Szám:"))
jo = (n % 10) % 3 == 0
while not jo :
        n = int(input ("Szám:"))
        jo = (n % 10) % 3 == 0