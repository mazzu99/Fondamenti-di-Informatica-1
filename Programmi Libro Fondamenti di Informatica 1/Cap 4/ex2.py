#Esercizio 2

s1 = input("Prima stringa: ")
s2 = input("Seconda stringa: ")

if s2 in s1:
    aus = s1.count(s2)
    print("La stringa ", s2, "compare ", aus, "volte nella stringa ", s1)
else:
    print("La stringa ", s2, "non compare ", "nella stringa ", s1)

