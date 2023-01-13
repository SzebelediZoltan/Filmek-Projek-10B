def fact(n):
    if n < 0:
        # return "Negatív paraméter!"
        return -1
    else:
        eredmeny=1
        for i in range(1,n+1):
            eredmeny=eredmeny*i
        return eredmeny

print(fact(-3))
print(fact(5))


# 10 allat 3?
n_alatt_k= fact(10)/(fact(3)*fact(7))
print(n_alatt_k)

