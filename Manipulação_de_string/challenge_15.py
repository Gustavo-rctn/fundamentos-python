def validar_especie(animal):
    if animal.isalpha():
        return "Espécie de animal válida."
    else:
        return "Espécie inválida."

# Exemplos de teste
print(validar_especie("Gato"))
print(validar_especie("Cachorro86"))