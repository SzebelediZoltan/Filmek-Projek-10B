n = int(input("Szám:"))


for i in range (n,1001):
    if (1001-i) % n == 0 :
        print ((1001)-i, end= " ")



# for i in range (999, 0, -1):
#     if i % n == 0:
#         print (i, end = " ")
