# Solicita ao usuário que insira seu nome
nome = input("Qual é o seu nome? ")

# Solicita ao usuário que insira sua idade
idade = int(input("Quantos anos você tem? "))

# Verifica se o usuário é maior de idade
if idade >= 18:
    print(f"Olá, {nome}! Você é maior de idade.")
else:
    print(f"Olá, {nome}! Você é menor de idade.")