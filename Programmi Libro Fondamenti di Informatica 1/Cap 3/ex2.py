#Esercizio 2

s = input("Metti una stringa: ")
c1 = input("Metti il primo carattere: ")
c2 = input("Metti il secondo carattere: ")

replace = s.replace(c1, c2)
print(replace)

count = s.count(c1+c2)
print(count)
