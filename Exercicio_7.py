# 7. Faça um programa que leia nome e idade de 5 pessoas e coloque os nomes em uma lista e as idades em outra. 
# Apresente as duas listas preenchidas.
nomes = []
idades = []
for i in range(5):
    nome = input(" Digite o nome da pessoa: ")
    idade = int(input(" Digite a idade da pessoa: "))
    nomes.append(nome)
    idades.append(idade)
print(" Lista de nomes:", nomes)
print(" Lista de idades:", idades)

