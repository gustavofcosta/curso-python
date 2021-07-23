''' # opçao 1
ef area():
    print('Controle de Terrenos')
    print('--' * 10)
    l = float(input('LARGURA (m): '))
    c = float(input('COMPRIMENTO (m): '))
    print(f'A área de um terreno {l}x{c} é de {l * c}m²')


area()

'''

def area(larg, comp):
    a = larg * comp
    print(f'A área de um terreno {larg}x{comp} é de {a}m²')


print('Controle de Terrenos')
print('--' * 10)
l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))
area(l, c)