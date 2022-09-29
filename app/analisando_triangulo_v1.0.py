print('-=' * 16)
analise = '     Analisador de Triângulos'
print(analise)
print('-=' * 16)

n1 = float(input('Primeiro segmento: '))
n2 = float(input('Segundo segmento: '))
n3 = float(input('Terceiro segmento: '))

if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2:
    print('Os segmentos acima PODEM FORMAR UM TRIÂNGULO!')
else:
    print('Os segumentos acima NÃO podem formar um triângulo.')
