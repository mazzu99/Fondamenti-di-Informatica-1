#Esercizio 1 parte 2

c = True
i = 0
s1 = input("Inserisci stringa: ")

while c:
    if s1 == "":
        c = False
    s1 = input("Inserisci stringa: ")
    i = i + 1
print(i-1)
