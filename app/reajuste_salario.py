# Reajuste no Salário

salário_funcionário = float(input('Qual é o salário do Funcionário? R$'))
aumento = salário_funcionário + (salário_funcionário * 15 / 100)

print(f'Um funcionário que ganhava R${salário_funcionário:.2f}, com 15% de aumento, passa a receber R${aumento:.2f}.')
