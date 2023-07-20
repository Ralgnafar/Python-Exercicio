# 3. Faça um programa que leia 10 números do usuário e os coloque corretamente no dicionário D abaixo.
# D = {'pares': [], 'impares':[]}
D = {'pares': [], 'impares': []}  # Dicionário para armazenar os números pares e ímpares
for i in range(10):
    numero = int(input(" Digite um número: ")) 
    if numero % 2 == 0:  
        D['pares'].append(numero)
    else:
        D['impares'].append(numero)
print(" Números pares:", D['pares'])
print(" Números ímpares:", D['impares'])
