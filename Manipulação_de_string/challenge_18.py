def validar_senha(senha):
    tem_tamanho = len(senha) >= 8
    tem_letra = any(char.isalpha() for char in senha)
    tem_numero = any(char.isdigit() for char in senha)
    tem_espaco = any(char.isspace() for char in senha)

    if tem_tamanho and tem_letra and tem_numero and not tem_espaco:
        return "Senha válida!"
    else:
        return "Senha inválida!"

# Exemplos de teste
print(f"Senha: python123 -> Resultado: {validar_senha('python123')}")
print(f"Senha: python -> Resultado: {validar_senha('python')}")
print(f"Senha: python 123 -> Resultado: {validar_senha('python 123')}")