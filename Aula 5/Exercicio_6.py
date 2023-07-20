# 6. Copie a lista "lista_concatenada" para uma nova lista chamada "copia_lista_concatenada" sem utilizar o operador de atribuição direta.
minha_lista = list(range(1, 11))
numeros_pares = list(range(0, 21, 2))
numeros_pares = [numero for numero in numeros_pares if numero % 5 != 0]
lista_concatenada = minha_lista + numeros_pares
copia_lista_concatenada = lista_concatenada.copy()
print(copia_lista_concatenada)
