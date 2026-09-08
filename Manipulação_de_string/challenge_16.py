def verificar_extensao(nome_arquivo):
    if nome_arquivo.endswith(".pdf"):
        return "Arquivo válido."
    else:
        return "Arquivo inválido."

# Exemplos de teste
print(verificar_extensao("relatorio.pdf"))
print(verificar_extensao("despesas.xlsx"))