# 1. Adicione os números de 1 a 10 à lista "minha_lista" utilizando um loop, em seguida 
#imprima esses valores na tela e por fim mostre o tamanho dessa lista.
minha_lista = []
# Adicionando os números de 1 a 10 à lista usando um loop
for i in range(1, 11):
    minha_lista.append(i)
    minha_lista
# Imprimindo os valores da lista
for numero in minha_lista:
    print(numero)
# Mostrando o tamanho da lista
tamanho_lista = len(minha_lista)
print("Tamanho da lista:", tamanho_lista)