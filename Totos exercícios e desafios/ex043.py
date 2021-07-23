peso = float(input('Informe seu peso: '))
altura = float(input('Informe sua altura: '))

imc = peso / (altura * altura)

if imc < 18.5:
  print('Você esta abaixo do peso ideal')
elif imc >= 18.5 and imc < 25:
  print('Você esta no peso ideal')
elif imc >= 25 and imc < 30:
  print('Você esta com sobrepeso')
elif imc >= 30 and imc < 40:
  print('Você esta com obesidade')
else:
  print('Você esta com obesisade mórbida')