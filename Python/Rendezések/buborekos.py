def buborékos(x):
    # i= meddig megyunk
    # i= mi az utolso indexu amit hasonlitunk
    for i in range(len(x)-1, 0, -1):
        for j in range(i):
            if x[j] > x[j+1]:
                x[j], x[j+1]= x[j+1], x[j] #csere 
                
def main():
    x=[3, 5, 2, 1, 3]
    print(x)
    buborékos(x)
    print(x)


# main()