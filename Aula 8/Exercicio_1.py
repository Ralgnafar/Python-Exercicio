# 1. Escreva uma função que retorne o maior número entre dois números.
def maior_numero(a, b):
    if a > b:
        return a
    else:
        return b
n1 = float(input(" Digite o primeiro número: "))
n2 = float(input(" Digite o segundo número: "))
maior_numero = maior_numero(n1, n2)
print(" O maior número é:", maior_numero)

