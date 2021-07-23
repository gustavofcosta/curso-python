import math

angulo = float(input('Digite um ângulo qualquer :'))

radi = math.radians(angulo)

print('O valor do seno é {:.2f} o valor do cosseno é {:.2} e o valor da tangente é {:.2}'.format(math.sin(radi), math.cos(radi), math.tan(radi)))
