# 4.Faça um programa que recebe uma string e retorna ela ao contrário. 
# Exemplo: Recebe "teste" e retorna "etset".
palavra = input(" Digite uma palavra: ")
palavra_lista = list(palavra)
palavra_lista = palavra_lista[::-1]
palavra = "".join(palavra_lista)
print(palavra)
