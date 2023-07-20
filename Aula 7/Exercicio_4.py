# 4. Faça um programa, utilizando Dicionários, que peça para o usuário inserir o nome de três produtos 
# de mercado e seus respectivos preços e os mostre na tela.
produtos = {}  
for i in range(3):
    nome_produto = input(" Digite o nome do produto: ")
    preco_produto = float(input(" Digite o preço do produto: R$"))
    produtos[nome_produto] = preco_produto
print(" Produtos de mercado e seus respectivos preços: ")
for produto, preco in produtos.items():
    print(f"{produto}: R${preco:.2f}")
