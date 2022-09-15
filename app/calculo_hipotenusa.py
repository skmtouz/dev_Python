# Resolvendo a Hipotenusa

'''CatetoOposto = float(input('Qual o comprimento do cateto oposto: '))
CatetoAdjacente = float(input('Qual o comprimento do cateto adjacente: '))
Hipotenusa = (CatetoOposto ** 2 + CatetoAdjacente ** 2) ** (1/2)

print(f'O comprimento da hipotenusa é {Hipotenusa:.2f}')'''

# import math

from math import hypot

CatetoOposto = float(input('Qual o comprimento do cateto oposto: '))
CatetoAdjacente = float(input('Qual o comprimento do cateto adjacente: '))
Hipotenusa = hypot(CatetoOposto, CatetoAdjacente)
print(f'A hipotenusa é {Hipotenusa:.2f}')