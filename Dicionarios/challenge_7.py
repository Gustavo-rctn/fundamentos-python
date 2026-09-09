def verificacao_aprovacao():
    aluno = {
        'nome': 'gustavo',
        'media': 8.8,
        'frequencia': 88
    }

    if aluno['media'] >= 7 and aluno['frequencia'] >= 75:
        print(f" O aluno {aluno['nome'].title()} foi APROVADO!\n"
              f"Média {aluno['media']}\n"
              f"Frequência {aluno['frequencia']}%.")
    else:
        print(f"O aluno {aluno['nome'].title()} foi REPROVADO com média {aluno['media']} e frequência {aluno['frequencia']}%.")


verificacao_aprovacao()