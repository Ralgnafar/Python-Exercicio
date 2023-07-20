# 12. Faça um programa que recebe um número inteiro do usuário e imprime na tela a quantidade 
# de divisores desse número e quais são eles.
numero = int(input(" Digite um número inteiro: "))
divisores = []
for i in range(1, numero + 1):
    if numero % i == 0:
        divisores.append(i)
quantidade_divisores = len(divisores)
print(" Quantidade de divisores: ", quantidade_divisores)
print(" Divisores: ", divisores)