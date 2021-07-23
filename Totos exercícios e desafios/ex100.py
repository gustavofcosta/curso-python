from random import randint
from time import sleep
# Fazer um programa que tenha uma lista chamada numeros
numeros = list() #ou []
# Fazer uma função sorteio que sorteie 5 numeros e devem ser colocanas em uma lista
def sorteio(lista):
    while len(numeros) < 5:
        random = randint(1, 10)
        if random in numeros:
            pass
        else:
            lista.append(random)
    print('Sorteando 5 valores da lista: ', end='')
    for n in lista:
        sleep(0.4)
        print(f'{n}', end=' ')
    print('PRONTO!')
# fazer uma função chamada somapar que vai somar todos valores pares sorteados pela função sorteio
def somapar(lista):
    s = 0
    for n in lista:
        if n % 2 == 0:
            s += n
    print(f'Somando os valores pares de {lista}, temos {s}')


sorteio(numeros)
somapar(numeros)
