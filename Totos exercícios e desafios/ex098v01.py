from time import sleep


def contador(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print('-='*20)
    print(f'Contagem de {i} até {f} de {p} em {p}')
    sleep(1)

    if i < f:
        c = i
        while c <= f:
            sleep(0.5)
            print(f'{c}', end=' ')
            c += p
        print('FIM!')
    else:
        c = i
        while c >= f:
            sleep(0.5)
            print(f'{c}', end=' ')
            c -= p
        print('FIM!')


contador(1, 10, 1)
contador(10, 0, 2)
print('Agora é sua vez de personalizar a contagem')
a = int(input('Inicio: '))
b = int(input('Fim: '))
c = int(input('Passo: '))
contador(a, b, c)