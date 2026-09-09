def exercicio_16():
    compra = {
        "cliente": "Maria",
        "produtos": []
    }
    for i in range(5):
        item = input(f"Digite o {i + 1}º produto: ")
        compra["produtos"].append(item)

    print(f"\nCliente: {compra['cliente']}")
    print(f"Produtos comprados: {', '.join(compra['produtos'])}")


exercicio_16()