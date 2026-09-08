def separar_nome(nome_completo):
    nome = nome_completo.split()
    return nome

nome_completo_ask = input('Digite seu nome completo: ').title()

update_format = separar_nome(nome_completo_ask)
formatted = ' \n'.join(update_format)

print(f'Seu nome completo: {nome_completo_ask}\n'
      f'Nome semparado: \n{formatted}')