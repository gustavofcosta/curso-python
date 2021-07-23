from random import randint
print('='*30)
print('Vamos brincar de PAR ou  ÍMPAR?')
print('='*30)
c = 0
while True:
    #Jogador
    valor = int(input('Digite um valor: '))
    jogador = int(input(('''
PAR ou ÍMPAR
[1] - PAR
[2] - ÍMPAR
-> ''')))
    # Computador
    compuvalor = randint(1, 10)
    total = valor + compuvalor
    print('=' * 30)
    if jogador == 1:
        print(f'Você jogou {valor} e escolheu PAR')
        print(f'O computador jogou {compuvalor} escolheu ÌMPAR')
        if total % 2 == 0:
            print(f'A soma deu {total} e é PAR, vocè ganhou')
            c += 1
        elif total % 2 != 0:
            print(f'A soma deu {total} e é ÍMPAR, computador ganhou')
            if True:
                break
    elif jogador == 2:
        print(f'Você jogou {valor} e escolheu ÍMPAR')
        print(f'O computador jogou {compuvalor} escolheu PAR')
        if total % 2 == 0:
            print(f'A soma deu {total} e é PAR, computador ganhou')
            if True:
                break
        elif total % 2 != 0:
            print(f'A soma deu {total} e é ÍMPAR, você ganhou')
            c += 1
    print('='*30)
    print('Vamos jogar novoamente!')
print(f'Game Over --> você ganhou {c} vezes')

