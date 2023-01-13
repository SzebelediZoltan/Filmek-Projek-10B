n = 1
# for i in range (n, 50+1):
#     print ("."*n)
#     n= n+1

for i in range (1, 51):
    for j in range (1, i+1) :
        print (j*".", end = "")  
    print()