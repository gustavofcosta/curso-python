from time import sleep


def maior(* num):
    tam = len(num)
    maior_valor = max(num)
    print('-='*25)
    sleep(0.4)
    print('Analisando os valores passados...')
    sleep(1)
    if maior_valor == 0:
        print(f'Foram informados 0 valores ao todo.')
        print(f'O maior valor informado foi {maior_valor}')
    else:
        for n in num:
            sleep(0.4)
            print(f'{n}', end=' ')
        sleep(0.4)
        print(f'Foram informados {tam} valores ao todo.')
        print(f'O maior valor informado foi {maior_valor}.')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior(0)
