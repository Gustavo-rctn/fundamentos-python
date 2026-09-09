def cadastro_dinamico():
    dados = {}

    quantos_dados = int(input('Digite a quantidade de dados: '))

    for item in range(quantos_dados + 1):
        chave = input('Digite o nome da chave: ')
        valor = input(f'Digite o valor de {chave}: ')
        dados[chave] = valor


    print('Cadastro final: ', dados)


cadastro_dinamico()