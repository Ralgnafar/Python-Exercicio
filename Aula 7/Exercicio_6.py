# 6. Crie um dicionário vazio semana = {} e o complete com uma chave para cada dia da semana, tendo
#  como seu valor uma lista com as aulas que você tem nesse dia (sábado e domingo recebem listas vazias, ou você tem aula?).
semana = {}
dias = ['segunda', 'terça', 'quarta', 'quinta', 'sexta', 'sábado', 'domingo']
for dia in dias:
    if dia in ['sábado', 'domingo']:
        semana[dia] = []
    else:
        aulas = input(f" Digite as aulas de {dia}: ").split(',')
        semana[dia] = [aula.strip() for aula in aulas]
for dia, aulas in semana.items():
    print(dia.capitalize(), ":", ", ".join(aulas))
