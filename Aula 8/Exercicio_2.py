# 2. Faça uma função que retorne o reverso de um número inteiro informado.
# Por exemplo: 127 -> 721.
def numero_invertido():
    numero = input(" Digite um número: ")
    numero_invertido = numero[::-1]
    print(" O número invertido é:", numero_invertido)
numero_invertido()

