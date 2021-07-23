nome = str(input('Digite seu nome completo: ')).strip()
primeiro = nome.split()
print('Primeiro nome é: {} '.format(primeiro[0]))
print('Segundo nome é: {} '.format(primeiro[len(primeiro) - 1]))