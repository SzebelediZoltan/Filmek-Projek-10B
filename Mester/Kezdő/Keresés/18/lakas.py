n, a, b = list(map(int, (input().split())))
ar=[]
meret=[]


for i in range (n):
    sor = list(map(int, input().split()))
    ar.append(sor[1])
    meret.append(sor[0])

x = 0
while x<n and (ar[x] <= a or meret[x] <= b):
    x += 1

if x < n:
    print(x + 1)
else:
    print(0)
