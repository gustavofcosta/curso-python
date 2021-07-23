from time import sleep


def contador():
    print('-=' * 20)
    print('Contagem de 1 até 10 de 1 em 1')
    for c in range(1, 11):
        sleep(0.5)
        print(c, end=' ')
    print('FIM', end=' ')
    print()
    print('-=' * 20)

    print('Contagem de 10 até 0 de 2 em 2')
    for c in range(10, -1, -2):
        sleep(0.5)
        print(c, end=' ')
    print('FIM', end=' ')
    print()
    print('-=' * 20)


def contadorp(a, b, d):
    print(f'Contagem de {a} até {b} de {d} em {d}')
    for c in range(a, b, d):
        sleep(0.5)
        print(c, end=' ')
    print('FIM', end=' ')

contador()
print('Agora é sua vez de personalizar a contagem')
i = int(input('Inicio: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
print('-=' * 20)
contadorp(i, f, p)