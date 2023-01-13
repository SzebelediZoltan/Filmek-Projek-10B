n = int(input())
m1=[]
m2=[]

for i in range (n):
    sor = list(map(int, input().split()))
    m1.append(sor[0])
    m2.append(sor[1])

# for i in range (n):
#     if m1[i-2] > m2[i]:


i=1
while i < n and not(m1[i-1] > m2[i]):
    i+=1
if i < n :
    i = i + 1
else:
    i=-1
print(i)
    