# a = altura
# l = largura
# ar = área
# qu = quantidade de tinta

a = float(input('Digita a altura da parede: '))
l = float(input('Digita a largura da parede: '))

ar = a * l

qu = ar / 2

print('A área da parede é {:.2f}m², e precisará de {:.2f} litros de tinta'.format(ar, qu))

