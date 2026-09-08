def create_email(nome, sobrenome, dominio):
    email = nome + sobrenome + dominio
    email_low_case = email.lower()
    return email_low_case

name = input('Digite seu nome: ')
sobrenome = input('Digite seu sobrenome: ')
dominio_gmail = '@gmail.com'

update_format = create_email(name, sobrenome, dominio_gmail)

print(f'Seu nome: {name}\n'
      f'Seu sobrenome: {sobrenome}\n'
      f'Seu dominio: {dominio_gmail}\n'
      f'Seu email: {update_format}')

