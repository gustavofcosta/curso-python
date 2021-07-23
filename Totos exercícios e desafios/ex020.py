import random

a1 = input('Escreva o nome do aluno nº1: ')
a2 = input('Escreva o nome do aluno nº2: ')
a3 = input('Escreva o nome do aluno nº3: ')
a4 = input('Escreva o nome do aluno nº4: ')

escolha = [a1, a2, a3, a4]
random.shuffle(escolha)
print('A ordem de apresentação será')
print(escolha)