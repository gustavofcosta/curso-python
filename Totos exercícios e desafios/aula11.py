print("\033[1;31;43mOlá mundo!\033[m")


print("\033[4;30;45mOlá mundo!\033[m")

print('=-='*10)

nome = 'Gustavo'
print('Muito prazer em te conhecer, {}{}{}!!'.format('\033[1;32m', nome, '\033[m'))


print('=-='*10)

nome = 'Gustavo'
cores = {'limpa':'\33[m',
         'azul':'\33[34m',
         'amarelo':'\33[33m',
         'pretoebranco':'\33[7;30m'}
print('Muito prazer em te conhecer, {}{}{}!!'.format(cores['azul'], nome, cores['limpa']))