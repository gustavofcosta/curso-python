from random import randint
print('='*30)
print('Vamos brincar de PAR ou  ÍMPAR?')
print('='*30)
c = 0
while True:
    print('=' * 30)
    jogador = int(input('Diga um número: '))
    computador = randint(0, 11)
    total = computador + jogador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('PAR ou ÍMPAR: ')).upper().strip()[0]
    print(f'Você jogou {jogador} e o computador jogou {computador} e o total foi {total}')
    print('Deu PAR' if total % 2 == 0 else 'Deu ÍMPAR')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você venceu!')
            c += 1
        else:
            print('Você perdeu!')
            if True:
                break
    elif tipo == 'I':
        if total % 2 == 1:
           print('Você venceu!')
           c += 1
        else:
            print('Você perdeu!')
            if True:
                break
    print('Vamos jogar denovo...')
print('=' * 30)
print(f'GAME OVER!!   Você venceu {c} vezes')



