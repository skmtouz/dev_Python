# Aluguel de Carros

dias = int(input('Quantos dias alugados? '))
km = float(input('Quantos KM rodados? '))
diaria = (dias * 60) + (km * 0.15)
print(f'O total a pagar é de R${diaria:.2f}')