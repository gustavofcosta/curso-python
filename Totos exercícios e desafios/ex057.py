sexo = str(input('Informe seu sexo [M/F]: ')).strip().upper()[0]

while sexo not in 'FfmM':
    sexo = str(input(('Dados invalidos, informe novamente seu sexo: '))).strip().upper()[0]

print('Sexo cadastrado com sucesso')







