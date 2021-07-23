print('='*36)
print('TABUADA NA PAUMA DAS MÃOS!!!!')
print('='*36)
while True:
    print('-' * 30)
    valor = int(input('Quer ver a tabuada de qual número? -> '))
    print('-'*30)
    if valor < 0:
        break
    for c in range(1, 11):
        print(f'{c} x {valor} = {c * valor}')
print('Programa tabuada encerrado!')
