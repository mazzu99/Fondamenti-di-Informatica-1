#Esercizio 5

n = 0
i = 0
c = True

while c:
    n1 = input("Inserisci un numero: ")
    if n1 == "*":
        c = False
    elif int(n1) < 0:
        i = i + 1
    else:
        pass

print(i)

