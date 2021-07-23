lista = []
c = 1
while True:
    lista.append(int(input('Digite um número: ')))
    r = str(input('Quer continuar...[S/N]: '))
    if r in 'Nn':
        break
if 5 in lista:
    print('O número 5 esta na lista')
else:
    print('O número 5 não esta na lista')
print(f'Foram digitados {len(lista)} números')
lista.sort(reverse=True)
print(f'A lista em ordem decrescente é {lista}')