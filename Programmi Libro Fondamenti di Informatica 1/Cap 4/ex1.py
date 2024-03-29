#Esercizio 1

s1 = input("Prima stringa: ")
s2 = input("Seconda stringa: ")

if s1[0] >= s2[0]:
    print("Prima stringa: ", s2)
    print("Seconda stringa: ", s1)
else:
    print("Prima stringa: ", s1)
    print("Seconda stringa: ", s2)
    

if len(s1) >= len(s2):
    print("Prima stringa: ", s2)
    print("Seconda stringa: ", s1)
else:
    print("Prima stringa: ", s1)
    print("Seconda stringa: ", s2)
