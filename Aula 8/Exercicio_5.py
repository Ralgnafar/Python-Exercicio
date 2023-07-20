# 5.  Crie uma função e dê o nome pertinente para a mesma, essa função deve retornar um dicionário
# com os dados abaixo:
# Matricula - Nome      - Sexo - Departamento - TempoServiço - Salario
#     1     - Ana       -  F   -     TI       -      7       - 3200
#     2     - Beatriz   -  F   -     TI       -      4       - 3720
#     3     - Carla     -  F   -     TI       -      1       - 2100
#     4     - Daniela   -  F   -     RH       -      2       - 3920
#     5     - Emílio    -  M   -     RH       -      7       - 4235
#     6     - Fernando  -  M   -     RP       -      7       - 1200
#     7     - Gabriela  -  F   -     RP       -      8       - 7234.89
#     8     - Hernandes -  M   -     TI       -      6       - 4234.12

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

import pprint
dados_funcionarios = criar_dicionario_funcionarios()
pprint.pprint(dados_funcionarios)
print("")
print("")
