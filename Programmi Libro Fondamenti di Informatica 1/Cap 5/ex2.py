#Esercizio 2

c = True

while c:
    n1 = input("Inserisci numeri e inserisci * per poter terminare: ")
    if n1 == "*":
        c = False
    else:
        n1 = int(n1)
        if n1%2 == 0:
            print("Pari")
        else:
            print("Dispari")
    
