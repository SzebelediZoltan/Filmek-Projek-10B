def f():
    global x
    x=5
    print("Fv-ben:", x)

x=6
print("FV elott:", x)
f()
print("FV utan:, x")