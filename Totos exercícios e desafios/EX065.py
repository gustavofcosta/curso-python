sair = 'S'
media = quant = total = maior = menor = 0

while sair in 'sS':
    num = int(input('Digite um número: '))
    quant = quant + 1
    total = total + num
    if quant == 1:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    sair = str(input('Quer continuar [S/N] ')).upper().strip()
media = total / quant
print('A média dos {} números digitados é {:.1f}'.format(quant, media))
print('O maior número é {} e o menor número é {}'.format(maior, menor))
