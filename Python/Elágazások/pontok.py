elsocs = input("1. csapat neve: ")
elsop = float (input("Pontjaik: "))
masodikcs = input("2. csapat neve: ")
masodikp = float (input("Pontjaik: "))


if elsop > masodikp :
    print (elsocs, "nyert")

elif elsop < masodikp :
    print (masodikcs, "nyert")

else :
    print ("Döntetlen")    