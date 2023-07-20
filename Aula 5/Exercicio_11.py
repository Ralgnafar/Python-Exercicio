# 11. Faça um script que peça ao usuário para digitar um número n e some todos os números de 1 a n.
n = int(input(" Digite um número inteiro: "))
soma = 0
for i in range(1, n + 1):
    soma += i
print(" A soma de todos os números de 1 a", n, "é", soma)
