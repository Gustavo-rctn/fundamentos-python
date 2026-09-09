def exercicio_11():
    produto = {
        "nome": "Teclado",
        "preco": 100.00
    }
    print(f"Preço atual: R$ {produto['preco']:.2f}")
    porcentagem = float(input("Digite o percentual de aumento: "))

    produto["preco"] += produto["preco"] * (porcentagem / 100)
    print(f"Aumento: {porcentagem}%")
    print(f"Novo preço: R$ {produto['preco']:.2f}")


exercicio_11()