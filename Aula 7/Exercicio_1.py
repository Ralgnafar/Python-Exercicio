 #1. Construa um programa no qual o usuário informe o nome, a estatura e o peso de vários alunos
# de uma turma. Após o cadastro, o programa deve imprimir o nome e o IMC de cada aluno ordenados
# pelo nome do aluno. Sabe-se que IMC = peso/altura**2
alunos = []  # Lista para armazenar os alunos
# Loop para cadastrar os alunos
while True:
    nome = input(" Digite o nome do aluno (ou 'sair' para encerrar): ")
    if nome.lower() == 'sair':
        break
    estatura = float(input(" Digite a estatura do aluno (em metros): "))
    peso = float(input(" Digite o peso do aluno (em kg): "))
    aluno = {
        "nome": nome,
        "estatura": estatura,
        "peso": peso
    }
    alunos.append(aluno)
alunos.sort(key=lambda x: x['nome'])
for aluno in alunos:
    imc = aluno['peso'] / aluno['estatura'] ** 2
    print(f" Nome: {aluno['nome']}, IMC: {imc:.2f}")
