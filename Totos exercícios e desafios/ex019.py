import random

a1 = input('Escreva o nome do aluno nº1: ')
a2 = input('Escreva o nome do aluno nº2: ')
a3 = input('Escreva o nome do aluno nº3: ')
a4 = input('Escreva o nome do aluno nº4: ')

lista = [a1, a2, a3, a4]
escolhido = random.choice(lista)

print('O aluno sorteado é o(a) {}'.format(escolhido))