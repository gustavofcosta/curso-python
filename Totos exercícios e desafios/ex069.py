sair = ' '
contadormulheres = contadorhomens = contadoridade = 0
while sair not in 'N':
    print('-=' * 15)
    print('====CADASTRO DE PESSOAL====')
    print('-=' * 15)
    idade = int(input('Qual sua idade: '))
    if idade > 18:
        contadoridade += 1
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Qual seu sexo [M/F]: ')).upper().strip()
        if sexo == 'M':
            contadorhomens += 1
    if idade > 20 and sexo == 'M':
        contadormulheres += 1
    print('-='*15)
    sair = str(input('Quer continuar: ')).upper().strip()
print(f'{contadoridade} pessoas possuem mais de 18 anos')
print(f'{contadorhomens} homens foram cadastrados')
print(f'{contadormulheres} mulheres possuem menos de 20 anos')
