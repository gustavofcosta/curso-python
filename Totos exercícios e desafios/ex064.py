'''
MINHA FORMA DE FAZER O EXERCICO

print('='*35)
print('Informe os números para serem registrados.')
print('Digite [999] para finalizar.')
print('='*35)
num = 0
soma = 0
total = 0
while num != 999:
    num = int(input('Digite o numero: '))
    if num == 999:
        print('Registro finalizado!')
    elif num == 0:
        print('Valor invalido tente denovo!')
    else:
        total = total + num
        soma = soma + 1
print('Foram registrados {} números'.format(soma))
print('A soma dos {} números registrados foi {} números'.format(soma, total))

                         DO PROFESSOR LOGO ABAIXO

'''
print('='*35)
print('Informe os números para serem registrados.')
print('Digite [999] para finalizar.')
print('='*35)
num = 0
soma = 0
total = 0
num = int(input('Digite o numero: '))
while num != 999:
    total = total + num
    soma = soma + 1
    num = int(input('Digite o numero: '))
print('Foram registrados {} números'.format(soma))
print('A soma dos {} números registrados foi {} números'.format(soma, total))