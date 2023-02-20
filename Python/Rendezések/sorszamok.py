from random import randint

def rendez_forditva(x, sorsz):
    n=len(x)
    for i in range(n-1, 0, -1):
        for j in range(i):
            if x[j]<x[j+1]:
                x[j], x[j+1]=x[j+1], x[j]
                sorsz[j], sorsz[j+1]= sorsz[j+1], sorsz[j]


def feltolt(n):
    x = []
    for i in range(n):
        r = randint(50, 100)
        x.append(r)
    return x

def main():
    x = feltolt(20)
    sorsz = list(range(1, 21))
    
    print("Rendezes elott:")
    print(sorsz)
    print(x)
    
    rendez_forditva(x, sorsz)
    print("Rendezes utan:")
    print(sorsz)
    print(x)

    print("1.hely:", sorsz[0])
    print("2.hely:", sorsz[1])
    print("3.hely:", sorsz[2])
    
main()