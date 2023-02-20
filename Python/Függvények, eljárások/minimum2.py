def minimum(*s):
    if len(s)>0:
        m=s[0]
        for i in range(1,len(s)):
            if s[i]<m:
                m=s[i]
        return m
    return None

m= minimum(-6, 7, -1, 7, -3, 8)
print(m)

m2=minimum()
print(m2)

m3=minimum(4, 1, 8)
print(m3)