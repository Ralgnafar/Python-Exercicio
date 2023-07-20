def options():
    print('''Escolha uma opção:

            1. Cadastrar Fornecedor
            2. Listar Fornecedores
            3. Procurar dados Fornecedor
            4. Deletar Fornecedor
            0. Sair      
            ''')

def main():
    supplier = []

    while True:
        options()
        option = int(input('Selecione uma opção: '))
        if (option == 1):
            registration(supplier)
        elif (option == 2):
            display(supplier)
        elif (option == 3):
            search(supplier)
        elif (option == 4 and len(supplier) != 0):
            delete(supplier)
        elif (option == 0):
            break
        else:
            print('Opção inválida')

def registration(supllier):
    identifier = int((input('Informe ID: ')))
    name  = (input('Informe Nome: '))
    phone = (input('Informe Telefone: '))
    mail  = (input('Informe E-mail:  '))
    supllier.append((identifier, name, phone, mail))

def display(supplier):
    for supplier in supplier:
        identifier, name, phone, mail = supplier
        print(f'id: {identifier}, nome: {name}, telefone: {phone}, email: {mail}')

def search(supplier):
    identifier_search = int(input('Informe ID: '))
    for supplier in supplier:
        identifier, name, phone, mail = supplier
        if (identifier == identifier_search):
            print(f'id: {identifier}, nome: {name}, telefone: {phone}, email: {mail}')
            break
    else:
        print(f'{identifier_search} não localizado')

def delete(supplier):
    delete = int(str(input('Informe ID: ')))
    for supplier in supplier:
        identifier, name, phone, mail = supplier
        if (identifier == delete):
            identifier.pop(delete)
            name.pop(delete)
            phone.pop(delete)
            mail.pop(delete)
            print
    else:
        print(f'{delete} não localizado')
main()



