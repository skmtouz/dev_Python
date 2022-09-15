# Separando Digitos

n1 = int(input('Digite um número: '))
unidade = n1 // 1 % 10
dezena = n1 // 10 % 10
centena = n1 // 100 % 10
milhar = n1 // 1000 % 10

print(f'Analisando seu número {n1}')

print(f'Unidade: {unidade}')
print(f'Dezena: {dezena}')
print(f'Centena: {centena}')
print(f'Milhar: {milhar}')