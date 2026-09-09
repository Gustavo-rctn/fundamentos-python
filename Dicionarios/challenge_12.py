def exercicio_12():
    funcionario = {
        "nome": "Lucas",
        "idade": 30,
        "cargo": "Dev",
        "salario": 5000.0,
        "telefone": "99999-9999"
    }
    print("1. Antes da remoção:", funcionario)
    telefone_removido = funcionario.pop("telefone")
    print("2. Telefone removido:", telefone_removido)
    print("3. Depois da remoção:", funcionario)


exercicio_12()