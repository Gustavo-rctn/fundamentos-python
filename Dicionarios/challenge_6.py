import json

def calcular_media(notas):
    return sum(notas) / len(notas)


def cadastro_notas():
    alunos = {}

    alunos['nomes'] = input('Digite o nome da aluno(a): ')
    quantidade = int(input('Digite a quantidade de notas: '))

    alunos['notas'] = []

    for item in range(quantidade):
        alunos['notas'].append(float(input(f'Digite a nota {item + 1} do aluno: ')))

    alunos['media'] = calcular_media(alunos['notas'])
    print('Aluno cadastrado', json.dumps(alunos, indent=4))

cadastro_notas()
