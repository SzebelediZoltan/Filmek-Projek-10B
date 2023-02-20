x=[]
def minimum(s):
    if len(s)>0:
        m=s[0]
        for i in range(1,len(s)):
            if s[i]<m:
                m=s[i]
        return m
    return None

print(minimum(x))


