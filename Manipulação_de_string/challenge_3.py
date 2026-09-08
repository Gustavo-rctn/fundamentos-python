def formartar_nome(nome):
    name = nome.title()
    return name

name_ask = input('Digite seu nome inteiro: ')

update_formatted = formartar_nome(name_ask)

print(f'Nome formatado: {update_formatted}\n'
      f'Nome do jeito digitado: {name_ask}')