dado = []
pessoa = []
maior = menor = c = tot = 0
while True:
    dado.append(str(input('Nome: ')))
    dado.append(float(input('Peso: ')))
    if len(pessoa) == 0:
        maior = menor = dado[1]
    else:
        if dado[1] > maior:
            maior = dado[1]
        if dado[1] < menor:
            menor = dado[1]
    pessoa.append(dado[:])
    dado.clear()
    tot += 1
    print('--' * 30)
    r = str(input(('Quer Continuar? [S/N]: ')))
    if r in 'Nn':
        break
print(f'Foram cadastradas {tot} pessoas')
print('-='*30)
print(f'O maior peso foi de {maior}Kg, peso de ', end='')
for p in pessoa:
    if p[1] == maior:
        print(f'[{p[0]}]',end='')
print()
print(f'O maior peso fooi de {menor}Kg, peso de ', end='')
for p in pessoa:
    if p[1] == menor:
        print(f'[{p[0]}]', end='')
print()
