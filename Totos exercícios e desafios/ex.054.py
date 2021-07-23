from datetime import date
date = date.today().year

maior = 0
menor = 0

for c in range(1, 8):
    ano = int(input('{}ª ano de nascimento: '.format(c)))
    idade = date - ano

    if idade < 21:
        menor = menor + 1

    else:
        maior = maior + 1
print('{} ainda não atingiram a maioridade'.format(menor))
print('{} pessoas ja atingiram a maioridadede'.format(maior))