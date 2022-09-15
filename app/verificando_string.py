# Verificando uma string

nome = str(input('Qual é seu nome completo? ')).strip()
print(f'Seu nome tem Souza? {"souza" in nome.lower()}')
