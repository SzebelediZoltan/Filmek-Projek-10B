n= int(input())
k=[]
f=[]

for i in range (n):
    sor = list(map(int, input().split()))
    k.append(sor[0])
    f.append(sor[1])
    
m = 0
for i in range (1,n):
    if k[i]>k[m]:
        m=i
print(f[m])