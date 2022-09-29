distância = float(input('Qual é a distância da sua viagem? '))
print(f'Você está prestes a começar uma viagem de {distância}Km.')

if distância <= 200:
    preço = distância * 0.50
    print(f'O preço da sua passagem será de R${preço:.2f}')
else:
    preço = distância * 0.45
    print(f'O preço da sua passagem será de R${preço:.2f}')


'''# forma simplificada porém não muito recomendada
preço = distância * 0.50 if distância <= 200 else distância * 0.45'''