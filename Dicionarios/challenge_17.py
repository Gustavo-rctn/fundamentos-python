def exercicio_17():
    alunos = []
    for i in range(5):
        print(f"\n--- Cadastro do Aluno {i + 1} ---")
        nome = input("Nome: ")
        idade = int(input("Idade: "))
        nota = float(input("Nota: "))

        alunos.append({
            "nome": nome,
            "idade": idade,
            "nota": nota
        })

    print("\n=== Lista de Alunos ===")
    for aluno in alunos:
        print(f"Nome: {aluno['nome']} | Idade: {aluno['idade']} | Nota: {aluno['nota']}")


exercicio_17()