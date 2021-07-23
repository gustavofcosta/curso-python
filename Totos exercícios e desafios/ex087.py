matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite uma valor para [{l}], [{c}]: '))
print('=-'*25)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
print('=-'*25)
soma = 0
for v, n in enumerate(matriz):
    for nu in (n):
        if nu % 2 == 0:
            soma += nu
print(f'A soma dos valores pares é {soma}')
somac = matriz[0][2] + matriz[1][2] + matriz[2][2]
print(f'A soma da terceira coluna é {somac}')
somal = matriz[1][0] + matriz[1][1] + matriz[1][2]
print(f'A soma da secunda linha é {somal}')


