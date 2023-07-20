# 5. Escreva um programa que duas strings e gere uma terceira na qual os caracteres da segunda foram retirados da primeira.
string1 = input(" Digite a primeira string: ")
string2 = input(" Digite a segunda string: ")
string3 = ""
for letra in string1:
    if letra not in string2:
        string3 += letra
if string3 == "":
    print(" Todos os caracteres foram removidos. ")
else:
    print(f" Os caracteres {string2} foram removidos de {string1}, gerando: {string3}")