lista = []
impares = []
pares = []
while True:
    lista.append(int(input('Digite um número: ')))
    reset = str(input('Quer continuar [S/N]?...'))
    if reset in 'Nn':
        break
for i, v in enumerate(lista):
    if v % 2 == 0:
        pares.append(v)
    else:
        impares.append(v)
print(f'O conjunto de lista é {lista}')
print(f'Os números pares da lista são {pares}')
print(f'Os números impares da lista são {impares}')

