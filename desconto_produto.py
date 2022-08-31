# Desconto de 5%

preço_produto = float(input('Qual é o preço do produto? R$'))
preço_desconto = preço_produto - (preço_produto * 5 / 100)
print(f'O produto que custava R${preço_produto:.2f}, na promoção com desconto de 5% vai custar R${preço_desconto:.2f}.')
