# 4. Faça uma função que verifique se um valor é perfeito ou não.
# Um valor é dito perfeito quando ele é igual a soma dos seus divisores excetuando ele próprio.
# (Ex: 6 é perfeito, 6 = 1 + 2 + 3, que são seus divisores). A função deve retornar um valor booleano.
def verificar_numero_perfeito():
    numero = int(input(" Digite um número: "))
    soma_divisores = 0
    for i in range(1, numero):
        if numero % i == 0:
            soma_divisores += i
    return soma_divisores == numero
resultado = verificar_numero_perfeito()
if resultado:
    print(" O número é perfeito.")
else:
    print(" O número não é perfeito.")
