def exercicio_13():
    funcionario = {
        "nome": "Mariana",
        "idade": 25,
        "cargo": "Designer",
        "salario": 4000.0,
        "telefone": "88888-8888"
    }
    chave_remover = input("Digite a chave que deseja remover: ").lower()

    if chave_remover in funcionario:
        del funcionario[chave_remover]
        print("Cadastro atualizado:", funcionario)
    else:
        print("Chave não encontrada.")


exercicio_13()