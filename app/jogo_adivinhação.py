from random import randint
from time import sleep
computer = randint(0, 5) # Variavel, faz o computador pensar em um número de 0 a 5
print('=' * 20)
print('Vou pensar em um número de 0 a 5. Tente adivinhar!')
print('=' * 20)
player = int(input('Em que número estou pensando? '))
print('Processando...')
sleep(3)

if player == computer:
    print('Parabéns, você acertou!')
else: print(f'Infelizmente você errou, o número que eu pensei foi {computer}')

