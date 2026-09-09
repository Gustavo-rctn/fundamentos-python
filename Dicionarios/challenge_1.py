def cadastro_pessoa():
    alunos = {
        'nome': 'Gustavo',
        'idade': 17,
        'telefone' : '(19) 99999-9999',
        'endereco' : {
            'cidade': 'Piracicaba',
            'numero': 511,
            'rua' : 'Dia de Luz'
        }
    }

    print('Nome: ', alunos.get('nome'))
    print('Idade: ', alunos.get('idade'))
    print('Telefone: ', alunos.get('telefone'))
    print('==== Endereço ====')
    print('Cidade: ',alunos['endereco'].get('cidade'))
    print('Rua: ',alunos['endereco'].get('rua'))
    print('numero: ',alunos['endereco'].get('numero'))


cadastro_pessoa()