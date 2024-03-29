#Esercizio 2

n = 0
c = True

while c:
    n1 = input("Inserisci un numero maggiore di 0: ")
    if n1 == "*":
        c = False
    elif int(n1) > n:
        n = int(n1)
    else:
        pass
print(n)
