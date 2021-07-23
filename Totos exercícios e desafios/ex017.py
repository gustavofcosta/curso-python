import math

cao = float(input('Qual o comprimento do cateto oposto de um triângulo retângulo: '))
caa = float(input('Qual o comprimento do cateto adjacente de um triângulo retângulo: '))


print('O valor da hipotenusa é: {}'.format(math.hypot(cao, caa)))

