import itertools

string = input("String a ser permutada: ")

resultado = itertools.permutations(string, len(string)) # Fara permutação dos caracteres no wordlist

for i in resultado:
    print("".join(i))