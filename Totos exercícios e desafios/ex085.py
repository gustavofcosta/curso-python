numeros = [[], []]
n = 0
for c in range(1, 8):
    n = int(input(f'Digite {c}ª valor: '))
    if n % 2 == 0:
        numeros[0].append(n)
    else:
        numeros[1].append(n)
print('=-'*30)
print(f'Os números pares são {sorted(numeros[0])}')
print(f'Os números impares são {sorted(numeros[1])}')
