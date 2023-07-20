# 8.Faça um script que leia números do usuário, enquanto ele não digitar 0. 
# Armazene esses números em uma lista e ao final informe quantos números foram digitados, ignorando o 0, 
# o valor máximo e o valor mínimo.
numeros = []
while True:
    numero = int(input(" Digite um número (0 para sair): "))
    if numero == 0:
        break 
    numeros.append(numero)
if numeros:
    quantidade_numeros = len(numeros)
    valor_maximo = max(numeros)
    valor_minimo = min(numeros) 
    print(" Quantidade de números digitados (excluindo o 0):", quantidade_numeros)
    print(" Valor máximo:", valor_maximo)
    print(" Valor mínimo:", valor_minimo)
else:
    print(" Nenhum número foi digitado (exceto o 0). ")