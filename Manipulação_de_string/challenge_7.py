def procurar_palavra(texto, palavra):
    frase_palavra = texto.find(palavra)
    return frase_palavra

frase_digitada = input('Digite uma frase: ')
palavra_find = str(input('Digite a palavra que você quer achar: '))

update_format = procurar_palavra(frase_digitada, palavra_find)

print(f'A frase digitada foi: {frase_digitada}\n'
      f'A palavra que você que achar é: {palavra_find}\n'
      f'A palavra aparece na posição: {update_format}')