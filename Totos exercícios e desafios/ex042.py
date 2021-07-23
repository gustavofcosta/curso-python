c1 = float(input('Informe o primeiro comprimento do triângulo: '))
c2 = float(input('Informe o segundo comprimento do triângulo: '))
c3 = float(input('Informe o terceiro comprimento do triângulo: '))

if c1 + c2 > c3 and c1 + c3 > c2 and c3 + c2 > c1:
  print('É possível formar um triângulo!')
  if c1 == c2 == c3:
    print('O triângulo é equilátero')
  elif c1 == c2 or c1 == c3 or c2 == c3:
    print('O triângulo é isósceles')
  else:
    print('O triangulo é escaleno')
else:
  print('Não é possível formar um triângulo')
