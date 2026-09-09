def ajuste_nome(nome):
    name = nome.strip().title()
    return name

name_ask = input('Digite seu nome: ')

update = ajuste_nome(name_ask)

print(f'Nome digitade: {name_ask}')
print(f'Nome formatado: {update}')


