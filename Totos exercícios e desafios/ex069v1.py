contadormulheres = contadorhomens = contadoridade = 0
while True:
        print('-=' * 15)
        print('====CADASTRO DE PESSOAL====')
        print('-=' * 15)
        idade = int(input('Qual sua idade: '))
        if idade >= 18:
            contadoridade += 1
        sexo = ' '
        while sexo not in 'MF':
            sexo = str(input('Qual seu sexo [M/F]: ')).upper().strip()[0]
            if sexo == 'M':
                contadorhomens += 1
        if idade > 20 and sexo == 'M':
            contadormulheres += 1
        print('-='*15)
        continuar = ' '
        while continuar not in 'SN':
            continuar = str(input('Quer continuar [S/N]: ')).upper().strip()[0]
        if continuar == 'N':
            break
print(f'{contadoridade} pessoas possuem mais de 18 anos')
print(f'{contadorhomens} homens foram cadastrados')
print(f'{contadormulheres} mulheres possuem menos de 20 anos')