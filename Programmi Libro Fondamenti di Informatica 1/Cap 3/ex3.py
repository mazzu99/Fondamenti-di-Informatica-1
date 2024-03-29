#Esercizio 3

s1 = input("Metti la prima stringa: ")
c1 = input("Metti il primo carattere: ")
s2 = input("Metti la seconda stringa: ")

replace = s1.replace(c1, "!!!")
print(replace)

count = s1.count(s2)
print(count)

replace = s1.replace(s2, c1)
print(replace)

