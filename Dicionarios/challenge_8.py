def exercicio_8():
    usuario_cadastrado = {
        "usuario": "admin",
        "senha": "123"
    }
    login = input("Digite o usuário: ")
    senha = input("Digite a senha: ")

    if login == usuario_cadastrado["usuario"] and senha == usuario_cadastrado["senha"]:
        print("Acesso permitido!")
    else:
        print("Usuário ou senha incorretos.")


exercicio_8()