k= int(input())

sz=[]
h=[]

for i in range (k):
    sor = list(map(int, input().split()))
    sz.append(sor[0])
    h.append(sor[1])
    
y=0
for i in range (k):
    x=sz[i]*h[i]
    y+=x
print(y)




