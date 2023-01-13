n=int(input())
nev=[]
magassag=[]
for i in range(n):
    sor=input().split()
    nev.append (sor[0])
    magassag.append (int(sor[1]))
# print(nev, magassag)

i=1
while i<n and not(magassag[i]<magassag[i-1]):
    i = i+1
if i<n:
    print("NEM")
else: 
    print("IGEN")


s=0
for i in range (n):
    s+= magassag[i]
# print(s)


x=s/n
print(x)



y=0
for i in range(n):
    if magassag[i]>x:
        y+=1
print(y)
