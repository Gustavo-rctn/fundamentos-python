def limpar_telefone(telefone):
    telefone_limpo = telefone.replace("(", "").replace(")", "").replace(" ", "").replace("-", "")
    return telefone_limpo

# Exemplo de teste
telefone = "(19) 99999-8888"
print(limpar_telefone(telefone))