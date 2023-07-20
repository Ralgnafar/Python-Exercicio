# 3. Crie uma lista chamada "lista_concatenada" que seja a concatenação das listas criadas na questão 1
# e na questão 2.
minha_lista = list(range(1, 11))
numeros_pares = list(range(0, 21, 2))
numeros_pares = [numero for numero in numeros_pares if numero % 5 != 0]
lista_concatenada = minha_lista + numeros_pares
print(lista_concatenada)

