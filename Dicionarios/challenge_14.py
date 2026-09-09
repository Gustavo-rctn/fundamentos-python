def exercicio_14():
    aluno = {
        "nome": "Carlos",
        "notas": [8.0, 7.5, 9.0]
    }
    notas = aluno["notas"]
    media = sum(notas) / len(notas)

    print(f"Nome do aluno: {aluno['nome']}")
    print(f"Todas as notas: {notas}")
    print(f"Maior nota: {max(notas)}")
    print(f"Menor nota: {min(notas)}")
    print(f"Média das notas: {media:.2f}")


exercicio_14()