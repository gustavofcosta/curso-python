print('='*28)
valores = list()
c = 0
for v in range(0, 5):
    valores.append(int(input('Digite um valor: ')))
maior = max(valores)
menor = min(valores)
print('=' * 28)
print(f'O maior valor foi {maior} e esta nas posições ',  end='')
for i, ve in enumerate(valores):
    if ve == maior:
        print(f'{i+1}...', end='')
print(f'\nO menor valor foi {menor} e esta nas posiçõs ', end='')
for i, ve in enumerate(valores):
    if ve == menor:
        print(f'{i+1}...', end='')
print()







