import random
print('Vamos jogar!')
print(' ')
num = int(input('Digite um numero de 1 a 5: '))


list = [1, 2, 3, 4, 5]
ran = random.choice(list)
print('O numero sorteado foi {}'.format(ran))


if num == ran:
    print('Você Venceu!')
else:
    print('O computador venceu!')