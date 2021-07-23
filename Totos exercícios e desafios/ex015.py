km = float(input('Qual a kilometragem percorrida?  '))
dias = int(input('Quantos dias ficou alugado?  '))

vkm = km * 0.15
vdias = dias * 60
print(" " * 5)
print('Valor por kilometro rodado R${:.2f}'.format(vkm))
print('Valor por dia alugado R${:.2f}'.format(vdias))

alu = vkm + vdias

print('Valor a pagar R${:.2f}'.format(alu))
print(" " * 5)