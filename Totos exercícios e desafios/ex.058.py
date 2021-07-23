from random import randint
print('-=-'*12)
print('Tente adivinhar um número de 0 a 10')
print('-=-'*12)
#Computador
computador = randint(0, 10)

acertou = False
palpite = 0

while not acertou:
    jogador = int(input('Qual sua jogada: '))
    palpite = palpite + 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... tente mais uma vez.')
        else:
            print('Menos... Tente mais uma vez.')
print('Você acertou com {} palpites'.format(palpite))