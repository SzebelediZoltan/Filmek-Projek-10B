n= int (input("n: "))
x=2
primE = True
while x < n and primE:
    if n % x == 0:
        primE = False 
        # print (x, end=" ")
        x+=1

if primE :
    print ("Prímszám")
else :
    print ("Nem prímszám")     
    
    