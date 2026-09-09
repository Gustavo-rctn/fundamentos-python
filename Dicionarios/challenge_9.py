def exercicio_9():
    cliente = {
        "nome": "Ana",
        "idade": 28,
        "cidade": "São Paulo"
    }
    info = input("Qual informação do cliente deseja consultar? ").lower()
    resultado = cliente.get(info, "Informação não encontrada.")
    print(resultado)


exercicio_9()