from random import * 
be = input ("Fej vagy Írás:")
if be !="F" and be!= "I":
    exit ()
erme = randint(1, 2) #1= fej 2=írás
if erme == 1: 
    vel = "F"
else: 
    vel = "I"
print()

print("Dobas:", vel )

if be == erme :
    print ("Nyertél!")
else: 
    print ("Vesztettél!")

