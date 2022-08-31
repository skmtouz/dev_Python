# SIMULADOR COM OS AMIGOS

from random import choice

p1 = str(input('Digite o nome do Primeiro Jogador: '))
p2 = str(input('Digite o nome do Segundo Jogador: '))
p3 = str(input('Digite o nome do Terceiro Jogador: '))
p4 = str(input('Digite o nome do Quarto Jogador: '))
p5 = str(input('Digite o nome do Quinto Jogador: '))
p6 = str(input('Digite o nome do Sexto Jogador: '))
p7 = str(input('Digite o nome do Sétimo Jogador: '))
p8 = str(input('Digite o nome do Oitavo Jogador: '))
p9 = str(input('Digite o nome do Nono Jogador: '))
p10 = str(input('Digite o nome do Décimo Jogador: '))

lista = [p1, p2, p3, p4, p5, p6, p7, p8, p9, p10]

resultado = choice(lista)
resultado2 = choice(lista)

print(f'O jogador {resultado} e o jogador {resultado2} vão começar jogando')