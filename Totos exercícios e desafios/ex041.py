from datetime import date
atual = date.today().year

nascimento = int(input('Informe seu ano de nascimento para saber sua categoria: '))

idade = atual - nascimento
print('Quem nasceu em {} possui {} anos'.format(nascimento, idade))

if idade >= 0 and idade <= 9:
    print('Sua categoria é MIRIM')
elif idade <= 14:
    print('Sua categoria é INFANTIL')
elif idade <= 19:
    print('Sua categoria é JUNIOR')
elif idade <= 25:
    print('Sua categoria é SÊNIOR')
else:
    print('Sua categoria é MASTER')
