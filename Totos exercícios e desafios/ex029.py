velo = float(input('Qual foi a velocidade do carro? '))
multa = (velo - 80) * 7
if velo > 80:
    print('Você foi multado, multa é de R${} reais'.format(multa))
