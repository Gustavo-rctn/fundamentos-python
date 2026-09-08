def limpar_texto(texto):
    limpo = texto.strip()
    return limpo

text = input('Digite uma frase: ')
update_formatted = limpar_texto(text)
print(f'Texto sem espaços no inicio nem no final: {update_formatted}\n'
      f'Texto do jeito que foi escrito: {text}')