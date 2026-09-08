def separar_dados(nome, idade, profissao, cidade):
    dados_pedidos = f'{nome}, {idade}, {profissao}, {cidade}'
    dados = dados_pedidos.split(', ')
    return dados

name = input('Digite seu nome: ').title().strip()
age = int(input('Digite sua idade: '))
profi = input('Digite seu profissao: ').title().strip()
city = input('Digite seu cidade: ').strip().title()

update_format = separar_dados(name, age, profi, city)

formatted = ', '.join(update_format)

print(formatted)


