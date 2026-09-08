def contar_letra(frase, letra):
    frase = frase.count(letra)
    return frase

frase_digitada = input('Digite uma frase: ')
letra_ask = input('Digite uma letra que você quer saber quantas vezes aparece: ')
update_format = contar_letra(frase_digitada, letra_ask)

print(f'A frase é: {frase_digitada}\n'
      f'A letra ({letra_ask}) apareceu {update_format} vezes')
