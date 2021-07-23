from random import randint
from time import sleep
print('-='*16)
print('------SIMULADOR MEGA SENA------')
print('-='*16)
sorteio = []
completo = []
jogos = int(input(('Quantos jogos você quer que eu sorteie? ==> ')))
print(f'=======<SORTEANDO {jogos} JOGOS>=======')
for c in range(0, jogos):
    rep = 0
    while True:
        ran = randint(1, 25)
        if ran not in sorteio:
            sorteio.append(ran)
            rep += 1
        if rep >= 15:
            break
    sorteio.sort()
    completo.append(sorteio[:])
    sorteio.clear()
njogo = 1
for l in completo:
    sleep(1)
    print(f'Jogo {njogo}: {l}')
    njogo += 1
sleep(1)
print('===========<BOA SORTE>===========')
