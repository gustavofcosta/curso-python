lista = []
while True:
    n = int(input('Digite um número: '))
    if n not in lista:
        lista.append(n)
        print('Valor adicionado com sucesso')
    else:
        print('Valor duplicado! Não vou adicionar...')
    continuar = str(input('Quer continuar [S/N]: '))
    if continuar in 'Nn':
        break
print(f'Você digitou os valores {sorted(lista)}')
