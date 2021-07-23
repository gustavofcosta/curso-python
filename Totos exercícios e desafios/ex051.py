ter = int(input('Informe o termo: '))
raz = int(input('Informe a razão: '))
dec = ter + (10 - 1) * raz
for c in range(ter, dec + 1, raz):
    print(c, end=' -> ')
print('FIM')


