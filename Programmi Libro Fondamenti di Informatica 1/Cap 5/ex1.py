#Esercizio 1

c = True

while c:
    s1 = input("Inserisci la stringa vuota se vuoi uscire: ")
    if s1 == "":
        c = False
    else:
        print(len(s1))
    
