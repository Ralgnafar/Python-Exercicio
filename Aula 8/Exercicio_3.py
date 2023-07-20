# 3. Faça um programa para imprimir:
#     1
#     1   2
#     1   2   3
#     .....
#     1   2   3   ...  n
# para um n informado pelo usuário. Use uma função que receba um valor x inteiro como parâmetro e imprima
# uma linha com 1 até x. 
# Se x = 1 na função, imprime:
# 1
# Se x = 2 na função, imprime:
# 1   2
# E assim por diante.
def numero_n(x):
  for i in range(1, x + 1):
    print(i)
n = int(input(" Digite um número para n: "))
numero_n(n)


