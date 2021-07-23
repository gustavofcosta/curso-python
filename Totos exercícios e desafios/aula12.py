nome = str(input('Qual é p seu nome? ')).title()
if nome == 'Gustavo':
    print('Que nome bonito')
elif nome == 'Paulo' or nome == 'Ana' or nome == 'João':
    print('Seu nome é bem popular no Brasil!')
else:
    print('Seu nome é bem normal!')
print('Tenha um bom dia {}!'.format(nome))
