print('-='*12)
print('CAIXA DE COMPRAS')
print('-='*12)
precom = barato = contador = totalp = totalc = 0

while True:
    produto = str(input('Informe o produto: '))
    preco = float(input('Informe o preço: '))
    print('-=' * 12)
    contador += 1
    totalc += preco
    if preco > 1000:
        totalp += 1
        barato = ' '
    if contador == 1:
        barato = produto
        precom = preco
    else:
        if preco < precom:
            precom = preco
            barato = produto
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar: ')).strip().upper()
    if continuar == 'N':
        break
    print('-=' * 12)
print(f'O total gasto na compra foi R${totalc}')
print(f'{totalp} produtos custou mais de R$1000 reais')
print(f'O produto mais barato é {barato} e seu preço é {preco}')
