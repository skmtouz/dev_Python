# Pintando a Parede

largura = float(input('Largura da parede: '))
altura = float(input('Altura da parede: '))
area = largura * altura
qtd_tinta = area / 2
print(f'Sua parede tem a dimensão de {largura:.1f}x{altura:.2f} e sua área é de {area}m².')
print(f'Para pintar essa parede, você precisará de {qtd_tinta:.2f}L de tinta.')