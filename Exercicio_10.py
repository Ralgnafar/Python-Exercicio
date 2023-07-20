# 10.Informe, de forma decrescente todos os pares entre N (número fornecido pelo usuário) e -N.
# Se N for par, ele também deve ser incluído no output (vide exemplo para N = 2)
N = int(input(" Digite um número inteiro: "))
if N % 2 == 1:
    N -= 1
for i in range(N, -(N + 1), -2):
    print(i)