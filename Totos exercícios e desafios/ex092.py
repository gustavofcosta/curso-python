from datetime import date
dicionario = dict()
dicionario['Nome'] = str(input('Nome: '))
dicionario['Ano de nascimento'] = int(input('Ano de nascimento: '))
dicionario['CTPS'] = int(input('Carteira de Trabalho ( 0 não tem): '))
if dicionario['CTPS'] != 0:
    dicionario['Ano de contratação'] = int(input('Ano de contratação: '))
    dicionario['Salário'] = int(input('Salário: '))
ano_atual = date.today().year
idade = ano_atual - dicionario['Ano de nascimento']
dicionario_novo = dict()
dicionario_novo['Nome'] = dicionario['Nome']
dicionario_novo['idade'] = idade
dicionario_novo['CTPS'] = dicionario['CTPS']
if dicionario_novo['CTPS'] != 0:
    dicionario_novo['Ano de contratação'] = dicionario['Ano de contratação']
    dicionario_novo['Salário'] = dicionario['Salário']
    tempodetrabalho = ano_atual - dicionario['Ano de contratação']
    apsentadoria = 35 - tempodetrabalho
    if tempodetrabalho >= 35:
        dicionario_novo['Aposentadoria'] = 'Aposentado(a)'
    else:
        dicionario_novo['Aposentadoria'] = idade + apsentadoria
print('-='*25)
for k, v in dicionario_novo.items():
    print(f'{k} tem valor {v}')