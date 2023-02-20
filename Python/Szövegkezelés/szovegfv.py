def nagybetusse(s):
    sz = ""
    for i in range(len(s)):
        if s[i] >= "a" and s[i] <= "z":
            # print(chr(ord(s[i])-32), end="")
            sz += chr(ord(s[i])-32)
        else:
            # print(s[i], end="")
            sz += s[i]
    return sz

#print -> '"'
#MO1
a = '"'
b = "'"
print(b + a + b)

#MO2
print("\'\"\'")

#MO3
# print(chr(39) + chr(34) + chr(39))
print(chr(ord("'")) + chr(ord('"')) + chr(ord("'")))

#Szovegfuggvenyek
varos = "Budapest"
nagybetus = varos.upper()
kisbetus = varos.lower()
cserelt = varos.swapcase()
print(varos, nagybetus, kisbetus, cserelt)

nev = "nemecsek erno"
tnev = nev.title()
print(nev, tnev)

mondat = "a mondatokat nagy kezdobetuvel kezdjuk."
nagymondat = mondat.capitalize()
print(mondat)
print(nagymondat)

#Sajat megoldas az upper() metodusra
sajat_nagybetus = nagybetusse(varos)
print(sajat_nagybetus)



#Logikai fuggvenyek
szoveg = "5m123"
if szoveg.isdigit():
    print("Csak szamjegyek!")
elif szoveg.isalpha():
    print("Csak betuk!")
elif szoveg.isalnum():
    print("Csak betuk es szamok!")
else:
    print("Van olyan karakter, ami nem betu es nem szam!")

sz="Budapest"
if sz.isupper():
    print("Csupa nagybetus!")
elif sz.islower():
    print("Csupa kisbetus!")
else:
    print("Van nagy es kis betu is!")

if sz.startswith("Buda"):
    print("Ezzel kezdodik: Buda")
if sz.endswith("pest"):
    print("Ezzel vegzodik: pest")

#Eltavolitasok
noveny= "almafa"
print("Kidobott {a, f}:", noveny.strip("af"))