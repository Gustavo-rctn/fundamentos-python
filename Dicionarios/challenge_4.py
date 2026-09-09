def verificando_chave():
    usuario = {
        'nome': 'Gustavo',
        'idade': 17,
        'email': 'gustavo@localhost.com',
        'senha': '12345',
        'endereco': {
            'cidade': 'Piracicaba',
            'rua': 'Das luzes',
            'numero': 511
        }
    }

    existe_ask = input('Digite um dado que quer saber do usuario: ').lower().strip().replace(' ', '')
    if existe_ask in usuario:
        print('Esse dado está no cadastro!\n'
              f'{'Dado: ', usuario.get(existe_ask)}\n')

    elif existe_ask not in usuario:
        print('Esse dado não existe!\n')

verificando_chave()