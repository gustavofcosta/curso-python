mu = 0
soma = 0
velho = 0
homen = ''
for p in range(1, 5):
    print('-=-' * 12)
    nome = str(input('Informe o nome da {}º pessoa: '.format(p))).strip()
    idade = int(input('Informa a idade da {}ª pessoa: '.format(p)))
    sexo = str(input('Informe o sexo da {}ª pessoa [M/F]: '.format(p))).strip().upper()


    # média de idade
    soma = soma + idade
    media = soma/4

    #O homen mais velho
    if sexo == 'M' and p == 1:
        velho = idade
        homen = nome

    if idade > velho and sexo == 'M':
        velho = idade
        homen = nome


    #Quantas mulher tem menos de 20 anos
    if sexo == 'F' and idade < 20:
        mu = mu + 1

#Resultados
print('-=-' * 12)
print('A média de idade do grupo é {}'.format(media))
print('O homen mais velho tem {} anos e é o {}'.format(velho, homen))
print('{} mulheres tem menos de 20 anos'.format(mu))
