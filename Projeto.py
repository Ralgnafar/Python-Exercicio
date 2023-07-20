fornecedores = {}

def adicionar_fornecedor():
    codigo = input("Digite o código do fornecedor: ")
    nome = input("Digite o nome do fornecedor: ")
    telefone = input("Digite o telefone do fornecedor: ")
    email = input("Digite o email do fornecedor: ")
    
    fornecedores[codigo] = {'Nome': nome, 'Telefone': telefone, 'Email': email}
    print("Fornecedor cadastrado com sucesso!")

def remover_fornecedor():
    if not fornecedores:
        print("Não há fornecedores cadastrados para remover.")
        return
    
    codigo = input("Digite o código do fornecedor que deseja remover: ")
    if codigo in fornecedores:
        del fornecedores[codigo]
        print("Fornecedor removido com sucesso!")
    else:
        print("Código de fornecedor não encontrado.")

def exibir_fornecedor():
    codigo = input("Digite o código do fornecedor que deseja exibir: ")
    fornecedor = fornecedores.get(codigo)
    if fornecedor:
        print("Informações do fornecedor:")
        print(f"Código: {codigo}")
        for chave, valor in fornecedor.items():
            print(f"{chave}: {valor}")
    else:
        print("Código de fornecedor não encontrado.")

def exibir_todos_fornecedores():
    if not fornecedores:
        print("Não há fornecedores cadastrados.")
        return
    
    print("Fornecedores cadastrados:")
    for codigo, fornecedor in fornecedores.items():
        print(f"Código: {codigo}")
        for chave, valor in fornecedor.items():
            print(f"{chave}: {valor}")
        print("------------------------")

while True:
    print("\n### Sistema de Cadastro de Fornecedores ###")
    print("1. Adicionar fornecedor")
    print("2. Remover fornecedor")
    print("3. Exibir informações de um fornecedor")
    print("4. Exibir todos os fornecedores cadastrados")
    print("0. Sair")
    
    opcao = input("Digite o número da opção desejada: ")
    
    if opcao == '1':
        adicionar_fornecedor()
    elif opcao == '2':
        remover_fornecedor()
    elif opcao == '3':
        exibir_fornecedor()
    elif opcao == '4':
        exibir_todos_fornecedores()
    elif opcao == '0':
        print("Saindo do sistema...")
        break
    else:
        print("Opção inválida. Tente novamente.")
