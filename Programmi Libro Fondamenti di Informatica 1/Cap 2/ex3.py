import math

#Esercizio 3: Inserisci il raggio e altezza di un cilindro e restituisci l'area.

r = int(input("Inserisci il valore del raggio: "))
a = int(input("Inserisci il valore dell'altezza: "))

area = math.pi * (r**2)
volume = area * a

print ("Area della base : ", area)
print ("Volume : ", volume)

