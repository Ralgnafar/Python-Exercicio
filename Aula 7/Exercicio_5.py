# 5. Escreva um programa que conta a quantidade de vogais em um 
# texto e armazena tal quantidade em um dicionário, onde a 
# chave é a vogal considerada.
texto = input(" Digite um texto: ")
contagem_vogais = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
for letra in texto:
    letra = letra.lower()  
    if letra in contagem_vogais:
        contagem_vogais[letra] += 1
print(" Contagem de vogais: ")
for vogal, quantidade in contagem_vogais.items():
    print(f"{vogal}: {quantidade}")
