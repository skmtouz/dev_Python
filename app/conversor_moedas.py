# Conversor de Moedas

real = float(input('Quanto de dinheiro você tem na conta? R$'))
dolar = real / 5.14
dolar_canadense = real / 3.97
euro = real / 5.08
libra = real / 6.03
iene = real / 0.037
peso_argentino = real / 0.037
baht_tailandes = real / 0.14

print('=' * 15)

print(f'Com R${real:.2f} reais você pode converter para US${dolar:.2f} Dolares')
print(f'Com R${real:.2f} reais você pode converter para ${dolar_canadense:.2f} Dolares Canadense')
print(f'Com R${real:.2f} reais você pode converter para €{euro:.2f} Euros')
print(f'Com R${real:.2f} reais você pode converter para £{libra:.2f} Libras')
print(f'Com R${real:.2f} reais você pode converter para ¥{iene:.2f} Ienes')
print(f'Com R${real:.2f} reais você pode converter para ${peso_argentino:.2f} Pesos Argentinos')
print(f'Com R${real:.2f} reais você pode converter para ฿{baht_tailandes:.2f} Baht Tailandês')

''' print('Com R${:.2f} reais você pode converter para US${:.2f} Dolares'.format(real, dolar))
print('Com R${:.2f} reais você pode converter para ${:.2f} Dolares Canadense'.format(real, dolar_canadense))
print('Com R${:.2f} reais você pode converter para €{:.2f} Euros'.format(real, euro))
print('Com R${:.2f} reais você pode converter para £{:.2f} Libras'.format(real, libra))
print('Com R${:.2f} reais você pode converter para ¥{:.2f} Ienes'.format(real, iene))
print('Com R${:.2f} reais você pode converter para ${:.2f} Pesos Argentinos'.format(real, peso_argentino))
print('Com R${:.2f} reais você pode converter para ฿{:.2f} Baht Tailandês'.format(real, baht_tailandes))'''

print('=' * 15)
