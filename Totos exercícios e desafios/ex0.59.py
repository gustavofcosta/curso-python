print('-=-'*12)
n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))
print('-=-'*12)

print('''
MENU
[1] - Somar
[2] - Multiplicar
[3] - Maior
[4] - Novos números
[5] - sair do progarma     
''')

sair = False
soma = 0
mul = 0
maior = 0
while not sair:
    opcao = int(input('Informe a opção desejada: '))
    print('-=-' * 12)
    if opcao == 5:
        sair = True
    else:
        if opcao == 1:
            soma = n1 + n2
            print('A opção escolhida foi 1 e a soma dos números é {}'.format(soma))
        elif opcao == 2:
            mul = n1 * n2
            print('A opção escolhida foi 2 e a multiplicação é {}'.format(mul))
        elif opcao == 3:
            if n1 > n2:
                print('{} é o maior número'.format(n1))
            elif n1 == n2:
                print('Os números são iguais.')
            else:
                print('{} é o maior número'.format(n2))
        elif opcao == 4:
            n1 = float(input('Digite o primeiro número: '))
            n2 = float(input('Digite o segundo número: '))
    print('-=-'*12)
print('Programa finalizado!')