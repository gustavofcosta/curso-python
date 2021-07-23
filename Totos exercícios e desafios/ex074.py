from random import randrange
numeros = (randrange(10), randrange(10), randrange(10),
     randrange(10), randrange(10))
print('Os números sorteados foram: ', end='')
menor = maior = n = c = 0
for cont in numeros:
    print(cont, end=' ')
print(f'\nO maior número é o {max(numeros)}')
print(f'O menor número é o {min(numeros)}')
