def exercicio_15():
    filme = {
        "titulo": "Inception",
        "ano": 2010,
        "genero": "Ficção Científica",
        "notas": []
    }
    for i in range(5):
        nota = float(input(f"Digite a {i + 1}ª nota do filme: "))
        filme["notas"].append(nota)

    media = sum(filme["notas"]) / len(filme["notas"])
    print(f"Filme: {filme['titulo']} | Média: {media:.2f}")


exercicio_15()