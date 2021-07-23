dis = float(input('Qual a distância da viagem em km '))

ate200 = (dis * 0.50)

mas200 = (dis * 0.45)

if dis <= 200:
    print('O Valor será de R${} reais'.format(ate200))
else:
    print('O valor será de R${} reais'.format(mas200))
