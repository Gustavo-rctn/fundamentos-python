def verificar_palavra(texto, palavra):
    frase_palavra = texto.find(palavra)
    if frase_palavra == -1:
        return "NÃO_ENCONTRADA"
    else:
        return "ENCONTRADA"

ask_texto = input("Digite uma frase: ")
ask_palavra = input("Digite a palavra a ser encontrada: ")

update_format = verificar_palavra(ask_texto, ask_palavra)

if update_format == "ENCONTRADA":
    print(f'A palavra {ask_palavra} foi encontrada!')
else:
    print(f'A palavra {ask_palavra} não foi encontrada!')
