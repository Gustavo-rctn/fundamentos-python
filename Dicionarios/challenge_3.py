def adicionando_informacoes():
    alunos = {
        'nome': 'Gustavo',
        'idade': 17,
        'email': 'gustavo@localhost.com',
        'telefone': input('Digite seu telefone: ').replace(' ', ' - '),
        'endereco': {
            'cidade': input('Digite o nome da cidade: ').title(),
            'rua': input('Digite o nome da rua: ').title(),
            'numero': int(input('Digite o nome da numero: '))
        }
    }
    print('Nome: ', alunos.get('nome'))
    print('Idade: ', alunos.get('idade'))
    print('E-mail: ', alunos.get('email'))
    print('Telefone: ', alunos.get('telefone'))
    print('Cidade: ', alunos['endereco'].get('cidade'))
    print('Rua: ', alunos['endereco'].get('rua'))
    print('Numero da Casa: ', alunos['endereco'].get('numero'))

adicionando_informacoes()