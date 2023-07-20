# 6. Com base no dicionário obtido na questão anterior, faça:
# a) Uma função que retorne o número de homens e mulheres cadastrados;
# b) Uma função que retorne um dicionário dos funcionários cujo tempo de serviço seja maior que 5 anos.
# c) Uma função que receba como argumento o sexo e retorne a média salarial dos funcionários daquele sexo.
import pprint
def criar_dicionario_funcionarios():
    funcionarios = {
        1: {'Matricula': 1, 'Nome': 'Ana', 'Sexo': 'F', 'Departamento': 'TI', 'TempoServico': 7, 'Salario': 3200},
        2: {'Matricula': 2, 'Nome': 'Beatriz', 'Sexo': 'F', 'Departamento': 'TI', 'TempoServico': 4, 'Salario': 3720},
        3: {'Matricula': 3, 'Nome': 'Carla', 'Sexo': 'F', 'Departamento': 'TI', 'TempoServico': 1, 'Salario': 2100},
        4: {'Matricula': 4, 'Nome': 'Daniela', 'Sexo': 'F', 'Departamento': 'RH', 'TempoServico': 2, 'Salario': 3920},
        5: {'Matricula': 5, 'Nome': 'Emílio', 'Sexo': 'M', 'Departamento': 'RH', 'TempoServico': 7, 'Salario': 4235},
        6: {'Matricula': 6, 'Nome': 'Fernando', 'Sexo': 'M', 'Departamento': 'RP', 'TempoServico': 7, 'Salario': 1200},
        7: {'Matricula': 7, 'Nome': 'Gabriela', 'Sexo': 'F', 'Departamento': 'RP', 'TempoServico': 8, 'Salario': 7234.89},
        8: {'Matricula': 8, 'Nome': 'Hernandes', 'Sexo': 'M', 'Departamento': 'TI', 'TempoServico': 6, 'Salario': 4234.12}
    }
    return funcionarios
def contar_generos(funcionarios):
    num_homem = 0
    num_mulher = 0
    for funcionario in funcionarios.values():
        if funcionario['Sexo'] == 'M':
            num_homem += 1
        elif funcionario['Sexo'] == 'F':
            num_mulher += 1
    return num_homem, num_mulher
def funcionarios_tempo_servico(funcionarios):
    funcionarios_mais_de_5_anos = {}
    for funcionario in funcionarios.values():
        if funcionario['TempoServico'] > 5:
            funcionarios_mais_de_5_anos[funcionario['Matricula']] = funcionario
    return funcionarios_mais_de_5_anos
def media_salarial_por_sexo(funcionarios, sexo):
    total_salarios = 0
    num_funcionarios = 0
    for funcionario in funcionarios.values():
        if funcionario['Sexo'] == sexo:
            total_salarios += funcionario['Salario']
            num_funcionarios += 1
    if num_funcionarios > 0:
        media_salarial = total_salarios / num_funcionarios
        return media_salarial
    else:
        return 0.0
dados_funcionarios = criar_dicionario_funcionarios()
# a) Número de homens e mulheres cadastrados
num_homem, num_mulher = contar_generos(dados_funcionarios)
print(" Letra a) ")
print(" Número de homens:", num_homem)
print(" Número de mulheres:", num_mulher)
print(" ")
# b) Funcionários com tempo de serviço maior que 5 anos
funcionarios_mais_de_5_anos = funcionarios_tempo_servico(dados_funcionarios)
print(" Funcionários com mais de 5 anos de serviço: ")
for funcionario in funcionarios_mais_de_5_anos.values():
    print(" Letra b) ")
    pprint.pprint(funcionario)
    print(" ")
# c) Média salarial por sexo
sexo = str.capitalize(input(" Dite o sexo desejado (F = Feminino ou M = Masculino: "))
media_salarial = media_salarial_por_sexo(dados_funcionarios, sexo)
print(" Letra c)  ")
if media_salarial > 0:
    print(f" Média salarial para o sexo {sexo}: {media_salarial:.2f}")
else:
    print(" Não há funcionários do sexo", sexo)