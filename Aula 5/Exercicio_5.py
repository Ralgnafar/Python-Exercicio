# 5. Crie uma lista chamada "lista_repetida" com 5 repetições da lista "lista_concatenada".
minha_lista = list(range(1, 11))
numeros_pares = list(range(0, 21, 2))
numeros_pares = [numero for numero in numeros_pares if numero % 5 != 0]
lista_concatenada = minha_lista + numeros_pares
lista_repetida = lista_concatenada * 5
print(lista_repetida)