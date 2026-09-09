def exercicio_10():
    produto = {
        "nome": "Mouse",
        "preco": 80,
        "estoque": 10
    }
    quantidade = int(input("Digite a quantidade vendida: "))

    if quantidade <= produto["estoque"]:
        produto["estoque"] -= quantidade
        print(f"Venda realizada! Estoque atual: {produto['estoque']}")
    else:
        print("Erro: Estoque insuficiente!")


exercicio_10()