def alterando_informacoes():
    alunos = {
        'nome': 'Gustavo',
        'idade': 17,
        'telefone': '(19) 99999-9999',
        'turma': '1',
        'curso': 'Desenvolvimento de Sistemas',
        'nota': [8.5, 9.0, 6.7, 7.5],
        'endereco': {
            'cidade': 'Piracicaba',
            'rua': 'Dia de Luz',
            'numero': 511
        }
    }
    print('Idade antes: ', alunos.get('idade'))
    alunos['idade'] = 18
    print('Idade atual: ', alunos.get('idade'))

    print('===================================================')

    print('Cidade antes: ', alunos['endereco'].get('cidade'))
    alunos['endereco']['cidade'] = 'São pedro'
    print('Cidade atual: ', alunos['endereco'].get('cidade'))



alterando_informacoes()
