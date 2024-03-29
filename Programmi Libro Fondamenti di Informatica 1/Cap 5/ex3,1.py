#Esercio 3 parte 1

s1 = input("Inserisci la stringa: ")
c1 = input("Inserisci il carattere: ")
i = 0
aus = s1

while i < len(s1):
    if s1[i] == c1:
        s1 = s1[:i] + s1[i+1:len(s1)]
        print(s1)
    i = i + 1
if s1 == aus:
    print(s1)
