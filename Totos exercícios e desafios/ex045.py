import random
import time
print('\033[33mVamos Jogar JOKENPÔ?\033[m')
itens = ('Pedra', 'Papel', 'Tesoura')
computador = random.randint(0, 2)
print('''Suas opções
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('Qual é sua jogada? '))
print('JO')
time.sleep(1)
print('KEN')
time.sleep(1)
print('PÔ!!!')
print('-='*11)
print('Computador jogou {}'.format(itens[computador]))
print('  Jogador  jogou {}'.format(itens[jogador]))
print('-='*11)

if computador == 0: # computador jogou PEDRA
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('Jogador GANHOU')
    elif jogador == 2:
        print('Computador GANHOU')
    else:
        print('Jogada invalida!')
elif computador == 1: # computador jogou PAPEL
    if jogador == 0:
        print('Computador GANHOU')
    if jogador == 1:
        print('EMPATE')
    if jogador == 2:
        print('Jogador GANHOU')
    else:
        print('Jogada invalida!')
elif computador == 2: # computador jogou TESOURA
    if jogador == 0:
        print('Jogador GANHOU')
    if jogador == 1:
        print('Computador GANHOU')
    if jogador == 2:
        print('EMPATE')
    else:
        print('Jogada invalida!')





