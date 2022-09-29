velocidade = float(input('Qual é a velocidade atual do carro? '))
multa = (velocidade - 80) * 7

if velocidade > 80:
    print('Você foi multado, o limite dessa via é 80Km/h!')
    print(f'Você deve pagar uma multa de R${multa:.2f}!')
else:
    print('Obrigado por respeitar o limite de velocidade, tenha uma boa viagem!')
