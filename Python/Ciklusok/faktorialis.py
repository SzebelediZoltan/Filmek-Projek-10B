n = int (input("n: "))

eredmeny = 1
for i in range (1, n+1): 
    
#    eredmeny = eredmeny * i 
    eredmeny *= i
print (n, "! = ", eredmeny, sep="")