produtos_sistema = []


def cadastrar_produto():
    nome = input("Nome do produto: ").strip()
    preco = float(input("Preço: R$ "))
    estoque = int(input("Quantidade em estoque: "))

    produtos_sistema.append({
        "nome": nome,
        "preco": preco,
        "estoque": estoque
    })
    print(f"Produto '{nome}' cadastrado com sucesso!")


def listar_produtos():
    if not produtos_sistema:
        print("Nenhum produto cadastrado.")
        return
    print("\n--- Produtos Cadastrados ---")
    for prod in produtos_sistema:
        print(f"Nome: {prod['nome']} | Preço: R$ {prod['preco']:.2f} | Estoque: {prod['estoque']}")


def buscar_produto():
    nome_busca = input("Nome do produto para buscar: ").strip().lower()
    for prod in produtos_sistema:
        if prod["nome"].lower() == nome_busca:
            print(f"Encontrado: {prod['nome']} | R$ {prod['preco']:.2f} | Estoque: {prod['estoque']}")
            return
    print("Produto não encontrado.")


def atualizar_estoque():
    nome_busca = input("Nome do produto: ").strip().lower()
    for prod in produtos_sistema:
        if prod["nome"].lower() == nome_busca:
            quantidade = int(input("Quantidade a alterar (positiva para aumentar, negativa para diminuir): "))
            novo_estoque = prod["estoque"] + quantidade
            if novo_estoque < 0:
                print("Operação cancelada: estoque não pode ficar negativo.")
            else:
                prod["estoque"] = novo_estoque
                print(f"Estoque atualizado! Novo total: {prod['estoque']}")
            return
    print("Produto não encontrado.")


def remover_produto():
    nome_busca = input("Nome do produto a remover: ").strip().lower()
    for prod in produtos_sistema:
        if prod["nome"].lower() == nome_busca:
            produtos_sistema.remove(prod)
            print("Produto removido com sucesso!")
            return
    print("Produto não encontrado.")


def exercicio_18():
    while True:
        print("\n===== SISTEMA DE PRODUTOS =====")
        print("1 - Cadastrar produto")
        print("2 - Listar produtos")
        print("3 - Buscar produto")
        print("4 - Atualizar estoque")
        print("5 - Remover produto")
        print("6 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_produto()
        elif opcao == "2":
            listar_produtos()
        elif opcao == "3":
            buscar_produto()
        elif opcao == "4":
            atualizar_estoque()
        elif opcao == "5":
            remover_produto()
        elif opcao == "6":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida, tente novamente.")


