# Teste de Condições

tempo = int(input('Quantos anos tem seu carro?'))
if tempo <= 3:
    print('Seu carro é muito novo')
else:
    print('Seu carro é muito velho')

print('=' * 20)

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2)/2
print(f'A sua média foi {m:.1f}')
if m >= 6.0:
    print('Sua média foi boa! PARABÉNS!')
else:
    print('Sua nota está abaixo da média, estude mais!')