dados = dict()
lista = list()
idadeacima = list()
# Ler nome, sexo e idade de varias pessoas
# guardar os dados de cada pessoa em um dicionario
# guardar todos os dicionarios em uma lista
tot = c = 0
mulheres = list()
while True:
    dados['Nome'] = str(input('Nome: ')).title()
    while True:
        dados['Sexo'] = str(input('Sexo [M/F]: ')).upper()[0]
        if dados['Sexo'] in 'MF':
            break
        print('Erro! Por favor, digite apenas M ou F.')
    dados['Idade'] = int(input('Idade: '))
    tot += dados['Idade']
    if dados['Sexo'] == 'F':
        mulheres.append(dados['Nome'])
    lista.append(dados.copy())
    c += 1
    while True:
        continuar = str(input('Quer continuar? [S/N]: ')).upper()[0]
        if continuar in 'SN':
            break
        print('Erro! Responda apenas S ou N.')
    if continuar == 'N':
       break
print('-='*25)
# Mostrar quantas pessoas foram cadastradas
print(f'- O grupo possui {c} pessoas.')
# A media de idade do grupo
media = tot / c
print(f'- A média de idade do grupo é de {media:5.2f}')
# Uma lista com todas as mulheres
print(f'- As mulheres cadastradas foram : ', end=' ')
for m in mulheres:
    print(m, end=' ')
print()
# Uma lista com todas as pessoas com idade acima da media
print('- Lista das pessoas que estão acima da média:')
for i in lista:
    if i['Idade'] > media:
        idadeacima.append(i.copy())
for d in idadeacima:
    for ii, k in d.items():
        print(f'{ii} = {k}; ', end=' ')
    print()
