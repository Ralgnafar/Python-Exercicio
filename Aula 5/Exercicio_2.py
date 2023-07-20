# 2. Crie uma lista com os números pares de 0 a 20 e em seguida atenda os seguintes comandos:
# a) Inverta a ordem dos elementos da lista.
# b) Inverta a ordem dos elementos da lista.
# c) Remova os números múltimos de 5 da lista.
numeros_pares = list(range(0, 21, 2))
print(" Números pares original: ", numeros_pares)
print((" Números pares invertida: ", numeros_pares[::-1]))
numeros_pares_sem_multiplos_de_5 = [numero for numero in numeros_pares[::-1] if numero % 5 != 0]
print(" Números pares sem múltiplos de 5: ", numeros_pares_sem_multiplos_de_5)


