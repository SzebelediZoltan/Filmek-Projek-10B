def f(s):
    return len(s)

gy = ["alma", "kiwi", "citrom", "áfonya", "barack", "pomelo", "grapefruit", "banan", "cigany meggy"]
gy.sort(key=f)
print(gy)
