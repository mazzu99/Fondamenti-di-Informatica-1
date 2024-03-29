#Esercizio 4

from random import *
n = int(input("Inserisci il range del valore n che sara' da indovinare (minimo 1): "))
nv = randint(1,n)

s1 = "Bravo hai indovinato"
s2 = "Il numero che hai detto e' tropo grande"
s3 = "Il numero che hai detto e' troppo piccolo"

n1 = int(input("Inserisci il primo tentativo: "))
if n1 == n:
    print(s1)
elif n1 > n:
    print (s2)
else:
    print(s3)



n2 = int(input("Inserisci il secondo tentativo: "))

if n2 == n:
    print(s1)
elif n2 > n:
    print (s2)
else:
    print(s3)



n3 = int(input("Inserisci il terzo tentativo: "))

if n3 == n:
    print(s1)
elif n3 > n:
    print (s2)
else:
    print(s3)
