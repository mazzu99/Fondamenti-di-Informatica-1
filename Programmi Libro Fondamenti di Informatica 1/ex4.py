#Esercizio 4

n = 0
i = 0
c = True

while c:
    n1 = input("Inserisci un numero maggiore di 0: ")
    if n1 == "*":
        c = False
    elif int(n1) > n:
        n = n + int(n1)
        i = i + 1
    else:
        pass
if n == 0:
    print("Non sono stati messi valori!!!")
else:
    print(n/i)
