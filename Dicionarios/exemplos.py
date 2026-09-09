def exibir_aluno():
    aluno = {
        'nome': 'Gustavo',
        'idade': 17,
        'curso': 'Desenvolvimento de Sistema'
    }
    print('nome:', aluno.get('nome'))
    print('idade:', aluno.get('idade'))
    print('curso:', aluno.get('curso'))
    print('nota:', aluno.get('nota'))


exibir_aluno()

print('==============================================================================')


# =======================================================================================
# Atualizando valores
def atualizar_idade():
    aluno = {
        'nome': 'Gustavo',
        'idade': 17,
        'curso': 'Desenvolvimento de Sistema'
    }

    print('idade antes: ', aluno.get('idade'))
    aluno['idade'] = 18
    print('Idade:', aluno.get('idade'))


atualizar_idade()

print('================================================================================')


# ==========================================================================================
def adicionar_informacao():
    aluno = {
        'nome': 'Gustavo',
        'idade': 25
    }
    print('Profissional antes:', aluno)
    aluno['nota'] = 9
    aluno['curso'] = 'Engenheiro de Software Senior/Staff'
    print('Profissional agora:', aluno)


adicionar_informacao()

print('===================================================================================')


# =======================================================================================
# verificando se uma chave existe
def verificar_chave():
    aluno = {
        'nome': 'Gustavo',
        'idade': 17
    }

    if 'nome' in aluno:
        print('O nome está cadastrado!')

    if 'nota' not in aluno:
        print('A nota não está cadastrada!')


verificar_chave()

print('===================================================================================')


# ======================================================================================
# utilizando comparações
def verificar_aprovacao():
    aluno = {
        'nome': 'Gustavo',
        'idade': 17,
        'nota': 9,
        'frequencia': 88
    }
    if aluno['nota'] >= 6 and aluno['frequencia'] >= 75:
        print(f"O aluno {aluno['nome']} foi aprovado!")
    else:
        print(f"O aluno {aluno['nome']} foi reprovado!")


verificar_aprovacao()

print('================================================================================')


# =========================================================================================
# Percorrendo as chaves
def listar_campos():
    produto = {
        'nome': 'Caneta Azul',
        'quantidade': 50,
        'preco_unitario': 1.25
    }
    for chave in produto.keys():
        print(chave)


listar_campos()

print('=================================================================================')


# ============================================================================================
# Percorrer os valores
def listar_valores():
    produto = {
        'nome': 'Caneta Azul',
        'quantidade': 50,
        'preco_unitario': 1.25
    }
    for valor in produto.values():
        print(valor)


listar_valores()
print('================================================================================')


# ========================================================================================
# Percorrendo chaves e valores
def exibir_produto():
    produto = {
        'nome': 'Caneta Azul',
        'quantidade': 50,
        'preco_unitario': 1.25
    }

    for chave, valor in produto.items():
        print(f'{chave}: {valor}')


exibir_produto()
print('================================================================================')


# ===========================================================================================
# atualizando e calculando
def atualizar_estoque():
    produto = {
        'nome': 'Caneta Azul',
        'quantidade': 50,
        'preco_unitario': 1.25
    }
    produto['total'] = produto['quantidade'] * produto['preco_unitario']
    print(f"O estoque todo do produto: {produto['nome']} \n Fica: {produto['total']}")


atualizar_estoque()
print('====================================================================================')


# ============================================================================================
def remover_estoque():
    produto = {
        'nome': 'Caneta Azul',
        'quantidade': 50,
        'preco_unitario': 1.25
    }
    nome = produto['nome']
    preco_unitario = produto['preco_unitario']

    del produto['nome']
    print(f"{nome} e {preco_unitario} foi removido do produto\n {produto}")

    print(preco_unitario)


# remover_estoque()

print('===================================================================================')


# ===========================================================================================
# lista de dicionarios
def listar_produtos():
    produtos = [
        {'nome': 'Teclado', 'preco': 299.00, 'quantidade': 2},
        {'nome': 'Mouse', 'preco': 199.00, 'quantidade': 3},
        {'nome': 'Monitor', 'preco': 1200.00, 'quantidade': 1}
    ]
    total_geral = 0
    for produto in produtos:
        print(f"O produto {produto['nome']} custa {produto['preco']}\n")
        total_individual = produto['preco'] * produto['quantidade']
        total_geral += total_individual

    print(f'O total geral é: {total_geral}')


listar_produtos()
print('====================================================================================')


# ============================================================================================
# Inserindo informação dinamicamente
def cadastrar_aluno():
    aluno = {}

    aluno['nome'] = input('Digite o nome do aluno: ').title()
    aluno['curso'] = input('Digite o curso do aluno: ').title()
    aluno['idade'] = int(input('Digite a idade do aluno: '))
    aluno['email'] = input('Digite o email do aluno: ')

    print(f'Dados cadastrados! Novo aluno: {aluno}')


# cadastrar_aluno()
print('================================================================================')


# ===========================================================================================
def criar_cadastro():
    dados = {}

    quantidade = int(input('Quantos dados você deseja cadastrar: '))

    for item in range(1, quantidade + 1):
        chave = input('Digite o nome do campo: ')
        valor = input(f'Digite o valor da {chave}: ')
        dados[chave] = valor

    print('Cadastro final: ', dados)


# criar_cadastro()
print('===================================================================================')


# ===========================================================================================
# dicionario com lista
def calcular_media(notas):
    return sum(notas) / len(notas)


def aluno_completo():
    aluno = {
        "nome": "Renan",
        "idade": 17,
        "curso": "Desenvolvimento de Sistemas",
        "notas": [8.5, 6.0, 9.3, 8.7],
        "endereco": {
            "cidade": "Piracicaba",
            "rua": "Das Amoreiras",
            "numero": 1257,
            "telefone": "(19) 98847-3687"
        }
    }
    aluno["media"] = calcular_media(aluno['notas'])
    print(aluno)


# aluno_completo()
print('===================================================================================')


# ====================================================================================================
import json

def cadastrar_dados_aluno():
    aluno = {}
    aluno['nome'] = input('Digite o nome do aluno: ')
    aluno['idade'] = int(input('Digite a idade do aluno: '))
    aluno['curso'] = input('Digite o curso: ')
    aluno['notas'] = []
    for item in range(4):
        aluno['notas'].append(float(input(f'Digite a nota {item + 1} do aluno: ')))

    aluno['endereco'] = {}
    aluno['endereco']['cidade'] = input('Digite o nome da sua cidade: ')
    aluno['endereco']['rua'] = input('Digite o nome da sua rua: ')
    aluno['endereco']['numero'] = int(input('Digite o numero da sua casa: '))
    aluno['endereco']['telefone'] = input('Digite o telefone da sua casa: ')

    aluno['media'] = calcular_media(aluno['notas'])
    print('Aluno cadastrado',json.dumps(aluno, indent=4))

cadastrar_dados_aluno()