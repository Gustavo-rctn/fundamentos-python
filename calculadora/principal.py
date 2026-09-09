from calculadora import dividir, multiplicar, somar, subtrair


def executar_calculadora():

    operacoes = {
        "1": somar,
        "2": subtrair,
        "3": multiplicar,
        "4": dividir
    }

    while True:
        print('===========CALCULADORA===========')
        print('*******ESCOLHA UMA OPÇÃO: *******')
        print('[1] - Somar')
        print('[2] - Subtrair')
        print('[3] - Multiplicar')
        print('[4] - Dividir')
        print('[0] - Sair')

        opcao = input('Escolha uma opção:')

        if opcao == '0':
            print('----CALCULADORA ENCERRADA----')
            break

        if opcao not in operacoes:
            print('OPÇÃO INVALIDA!')
            continue

        numero1 = float(input('Digite o primeiro valor: '))
        numero2 = float(input('Digite o segundo valor: '))

        funcao = operacoes[opcao]

        resultado = funcao(numero1, numero2)

        print(f'O resultado da operação é: {resultado}')

executar_calculadora()

