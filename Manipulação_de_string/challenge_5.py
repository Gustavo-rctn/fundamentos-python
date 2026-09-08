def substituir_palavra(frase, palavra_1, palavra_2):
    frase_nova = frase.replace(palavra_1, palavra_2)
    return frase_nova


frase_digitada = input('Digite uma frase que contenha a palavra Java: ')
palavra_1_java = 'Java'
palavra_2_python = 'Python'

update_format = substituir_palavra(frase_digitada, palavra_1_java, palavra_2_python)
print(f'A palavra sem replace: {frase_digitada}\n'
      f'Palavra formatada: {update_format}')
