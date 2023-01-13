x = [7, 9, 12, 3, -5, -2, 8, -5, 18, -1]
n= len(x)
#Parosak szama 
dbParos = 0
for i in range (n):
    if  x[i] % 2 == 0:
        # print(i)
        dbParos += 1

print(dbParos)

# Legnagyobb elem erteke
maxe = x [0]
for i in range (1, n):
    if x[i] > maxe:
        maxe = x[i]
print(maxe)

#Negativak szorzata
negativ = 1
for i in range (n):
    if x[i]< 0 :
        negativ *= x[i]
print(negativ)

# Legkisebb elem hol van

mine =0

for i in range (1,n):
    if x[i] <= x[mine]:
        mine = i
        
print(mine)

#Átlag


