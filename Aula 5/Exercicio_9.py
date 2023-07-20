# 9.Faça um script que informe o fatorial de um número.
# Utilize obrigatoriamente o comando for
numero = int(input(" Digite um número inteiro: "))
fatorial = 1
if numero < 0:
    print(" O fatorial não está definido para números negativos. ")
elif numero == 0:
    print(" O fatorial de 0 é 1. ")
else:
    for i in range(1, numero + 1):
        fatorial *= i
    print(" O fatorial de", numero, "é", fatorial)