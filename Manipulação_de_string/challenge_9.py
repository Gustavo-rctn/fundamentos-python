def contar_palavras(texto):
    frase_find = len(texto.split())
    return frase_find

frase_ask = input('Digite uma frase: ')

update_format = contar_palavras(frase_ask)
print(f'A frase {frase_ask} tem {update_format} palavras')