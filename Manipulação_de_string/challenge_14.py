def validar_telefone(numeros):
    if numeros.isdigit():
        return "Número de telefone válido!."
    else:
        return "Número inválido! Digite somente números."

# Exemplos de teste
print(validar_telefone("11988747584"))
print(validar_telefone("(11) 988747584"))